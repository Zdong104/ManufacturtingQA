# utils.py
import os
import pandas as pd
import re
from datetime import datetime
from PIL import Image
import matplotlib.pyplot as plt
import base64
from openai import OpenAI
import json
import openai
import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext

def plot_images(image_paths):
    images_shown = 0
    for img_path in image_paths:
        if os.path.isfile(img_path):
            image = Image.open(img_path).convert("RGB")

            plt.subplot(8, 8, images_shown + 1)
            plt.imshow(image)
            plt.xticks([])
            plt.yticks([])
            
            images_shown += 1
            if images_shown >= 64:
                break

    plt.tight_layout()
    plt.show()

# Build and load embeddings
def load_index_from_storage(args):
    from llama_index.core import load_index_from_storage, StorageContext
    openai.api_key = args.api_key

    # Load local Qdrant vector store
    ## RAG
    storage_context = StorageContext.from_defaults(persist_dir="3Experiment/3storage/storage")
    args.index = load_index_from_storage(storage_context)
    ##MMRAG
    client = qdrant_client.QdrantClient(path="3Experiment/3storage/MMqdrant_d")
    text_store = QdrantVectorStore(client=client, collection_name="text_collection")
    image_store = QdrantVectorStore(client=client, collection_name="image_collection")
    MMstorage_context = StorageContext.from_defaults(vector_store=text_store, image_store=image_store, persist_dir="3Experiment/3storage/MMstorage")
    args.MMindex = load_index_from_storage(MMstorage_context, image_store=image_store)
    return

def build_index(args):
    from llama_index.core import SimpleDirectoryReader
    from llama_index.core.indices import MultiModalVectorStoreIndex

    openai.api_key = args.api_key
    # Create a local Qdrant vector store
    ## RAG
    documents = SimpleDirectoryReader("1Book/3Book_txt_images",required_exts=[".txt"],recursive=True).load_data()
    index = VectorStoreIndex.from_documents(documents, chunk_size=600, chunk_overlap=100)
    index.storage_context.persist(persist_dir="3Experiment/3storage/storage") # Save the index to disk
    args.index = index
    ##MMRAG
    client = qdrant_client.QdrantClient(path="3Experiment/3storage/MMqdrant_d")
    text_store = QdrantVectorStore(client=client, collection_name="text_collection")
    image_store = QdrantVectorStore(client=client, collection_name="image_collection")
    MMstorage_context = StorageContext.from_defaults(vector_store=text_store, image_store=image_store)
    MMdocuments = SimpleDirectoryReader("1Book/3Book_txt_images").load_data()
    MMindex = MultiModalVectorStoreIndex.from_documents(MMdocuments, storage_context=MMstorage_context)
    # Save it
    MMindex.storage_context.persist(persist_dir="3Experiment/3storage/MMstorage")
    args.MMindex = MMindex
    return


# GPT Request Section
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def generate_response(args, query, image_paths):
    client = OpenAI(api_key=args.api_key)
    # No error will be raised if the image is not found
    encoded_images = [encode_image(img_path) for img_path in image_paths]

    # Construct the messages for the GPT-4 model
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                *[{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}"}} for img in encoded_images]
            ]
        }
    ]

    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=4000
    )

    return response.choices[0].message.content

# Function to retrieve prompt by type
def get_prompt_by_type(args):
    prompt_type = args.QAType
    # Load prompts from JSON file
    with open('3Experiment/2codes/prompts.json', 'r') as file:
        data = json.load(file)
    # Find the prompt based on the type
    prompt_data = next((item for item in data['prompts'] if item['index'] == prompt_type), None)
    if args.verbose: print(prompt_data)
    if prompt_data: 
        return prompt_data['content']
    else:
        return f"No prompt found for type: {prompt_type}"

# Function to parse the Explanation and YourChoice from each response
def parse_row(row):
    explanation_match = re.search(r'"Explanation": "(.*?)"', row)
    choice_match = re.search(r'"YourChoice": "(.*?)"', row)
    
    explanation = explanation_match.group(1) if explanation_match else ""
    choice = choice_match.group(1) if choice_match else ""
    
    return pd.Series([explanation, choice])


# Function to extract text and file paths from result.source_nodes and result.metadata
def extract_context_and_paths1(result):
    # Extract texts from source_nodes
    if isinstance(result, str):
        texts = [result]
        context = " ".join(texts)  # Concatenate all texts
        scores = "No scores found."
        file_paths = "No file paths found."
        context_path = "; ".join(file_paths)  # Join multiple file paths

    else:
        texts = [node.text for node in result.source_nodes]
        context = " ".join(texts)  # Concatenate all texts
        score = [node.score for node in result.source_nodes]
        scores = " ".join(str(score))
        file_paths = [node.metadata['file_path'] for node in result.source_nodes if 'file_path' in node.metadata]
        context_path = "; ".join(file_paths)  # Join multiple file paths
    return context, scores, context_path



# Function to extract text and file paths from result.source_nodes and result.metadata
def extract_context_and_paths2(result):
    """
    This function extracts context (text) and file paths from the result, which is now a NodeWithScore object.
    """
    # Check if result contains a node with text and metadata
    if isinstance(result, list) and len(result) > 0:
        # Initialize lists for texts and file paths
        texts = []
        scores = []
        file_paths = []
        
        for item in result:
            node = item.node  # Access the node inside NodeWithScore
            if hasattr(node, 'text'):  # Check if node has a 'text' attribute
                texts.append(node.text)
            if hasattr(item, 'score'):  # Check if score exists
                scores.append(item.score)
            if 'file_path' in node.metadata:
                file_paths.append(node.metadata['file_path'])
        
        # Join texts and file paths into single strings
        context = " ".join(texts) if texts else "No context found."
        score_str = ", ".join([str(score) for score in scores])  # Concatenate scores
        file_path_str = ", ".join(file_paths)  # Concatenate file paths
    
    else:
        context = "No context found."
        score_str = "No scores found."
        file_path_str = "No file paths found."

    return context, score_str, file_path_str

def data_processor(result_type, results, args):
    if args.QAType == 1:  # MCQ
        if result_type == "GPT_results":
            # Extract OutputAnswers from each result in results
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers'])
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer","OutputAnswers"]]
            return result_df
        
        elif result_type == "GPT_cot_results":
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers'])
            Outputs_df[['Explanation', 'YourChoice']] = Outputs_df['OutputAnswers'].apply(parse_row)
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer", "Explanation", "YourChoice", "OutputAnswers"]]
            return result_df
        
        else:
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers', 'Context','Confident_Score', 'Context_path'])
            Outputs_df[['Explanation', 'YourChoice']] = Outputs_df['OutputAnswers'].apply(parse_row)
            # Create lists for contexts and context paths
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer", "Explanation", "YourChoice", "OutputAnswers", "Context", "Context_path", "Confident_Score"]]
            return result_df
    elif args.QAType == 3:  # ImageQ:
        if result_type in ["GPT_results", "GPT_cot_results"]:
            # Extract OutputAnswers from each result in results
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers'])
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer","OutputAnswers","image_filename"]]
            return result_df
        
        else:
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers', 'Context','Confident_Score', 'Context_path'])
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer", "OutputAnswers", "Context", "Context_path", "Confident_Score","image_filename"]]
            return result_df
    elif args.QAType == 4:  # MathQ:
        if result_type in ["GPT_results", "GPT_cot_results"]:
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers'])
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer","OutputAnswers","chapter","question_number"]]
            return result_df
        
        else:
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers', 'Context','Confident_Score', 'Context_path'])
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer", "OutputAnswers", "Context", "Context_path", "Confident_Score","chapter","question_number"]]
            return result_df
    else:
        if result_type in ["GPT_results", "GPT_cot_results"]:
            # Extract OutputAnswers from each result in results
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers'])
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer","OutputAnswers"]]
            return result_df
        
        else:
            Outputs_df = pd.DataFrame(results, columns=['OutputAnswers', 'Context','Confident_Score', 'Context_path'])
            result_df = pd.concat([args.questions_df, Outputs_df], axis=1)
            result_df = result_df[["Question", "Answer", "OutputAnswers", "Context", "Context_path", "Confident_Score"]]
            return result_df
    
def save_results_to_folder(result_df, args, results_type):
    # Get the current datetime for filename
    now = datetime.now()
    timestamp = now.strftime("%Y_%m_%d_%H_%M")

    # Map QAType to the corresponding folder names
    qa_type_map = {
        1: "MCQ",
        2: "ResponseQ",
        3: "ImageQ",
        4: "MathQ"
    }
    
    # Determine the folder name based on QAType
    qa_type_folder = qa_type_map.get(args.QAType, "UnknownType")

    # Create the folder path
    folder_path = f"4Results/{qa_type_folder}"
    
    # Create the folder if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Generate the file name
    file_name = f"{results_type}_{timestamp}.csv"
    file_path = os.path.join(folder_path, file_name)
    
    # Save the DataFrame to CSV
    result_df.to_csv(file_path, index=False)
    
    print(f"Results saved to: {file_path}")

