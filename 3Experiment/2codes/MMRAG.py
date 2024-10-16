# MMRAG.py
import os
import re
import openai
import qdrant_client
from llama_index.core import SimpleDirectoryReader
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.indices import MultiModalVectorStoreIndex
from llama_index.core.schema import ImageNode
# Local imports
from utils import get_prompt_by_type, plot_images, generate_response, extract_context_and_paths1, extract_context_and_paths2
import pdb
def extract_image_links(text):
    pattern = r'!\[\]\((.*?)\)'
    return re.findall(pattern, text)


# Step 2: Modify paths to correct image paths
def full_image_paths(image_links, base_folder):
    text_extracted_images = []
    for img_path in image_links:
        img_path = os.path.basename(img_path)
        full_path = os.path.join(base_folder, img_path)

        if not os.path.isfile(full_path):
            print(f"File not found: {full_path}")
        text_extracted_images.append(full_path)
    return text_extracted_images


def retrive_document(args, img_from_text_only) -> str:
    from llama_index.core.response.notebook_utils import display_source_node
    from llama_index.core.schema import ImageNode
    if img_from_text_only:
        retriever = args.MMindex.as_retriever(similarity_top_k=args.top_k, image_similarity_top_k=0)
    else:
        retriever = args.MMindex.as_retriever(similarity_top_k=args.top_k, image_similarity_top_k=args.image_top_k)

    if args.interactive:
        args.question = input("Enter your question: ")
    try:
        retrieval_results = retriever.retrieve(args.question)
        images_link = []
        retrieved_images_todo = []
        context_str = ""
        for res_node in retrieval_results:
            if isinstance(res_node.node, ImageNode):
                retrieved_images_todo.append(res_node.node.metadata["file_path"])
            else:
                text = res_node.node.text
                context_str += text
                images_link += extract_image_links(text)
        retrieved_images = full_image_paths(retrieved_images_todo, base_folder="./1Book/3Book_txt_images")
        text_extracted_images = full_image_paths(images_link, base_folder="./1Book/3Book_txt_images")
        all_images = retrieved_images + text_extracted_images

        if args.verbose:
            print(context_str)
        if args.plot:
            plot_images(retrieved_images)
            print('Images paths:\n',all_images)

    except RuntimeError as e:
        # Check if the error message indicates that the input context is too long
        if 'too long for context length' in str(e):
            retrieval_results = "No output, likely because the input context is too long"
            context_str = "Context Not Available"
            all_images = []
            if args.verbose: print(retrieval_results)
        else:
            # If it's a different RuntimeError, raise it
            raise e
    return retrieval_results, context_str, all_images

def answer_question(args) -> str:
    # from llama_index.core.query_engine import SimpleMultiModalQueryEngines
    from llama_index.multi_modal_llms.openai import OpenAIMultiModal
    from llama_index.core.response.notebook_utils import display_source_node
    from llama_index.core import PromptTemplate
    openai_mm_llm = OpenAIMultiModal(model="gpt-4o", api_key=args.api_key, max_new_tokens=4000)
    new_summary_tmpl = PromptTemplate(get_prompt_by_type(args))
    MMquery_engine = args.MMindex.as_query_engine(llm=openai_mm_llm, text_qa_template=new_summary_tmpl, similarity_top_k=args.top_k, image_similarity_top_k=0)
    if args.interactive:
        args.question = input("Enter your question: ")
    try:
        result = MMquery_engine.query(args.question)
        if args.verbose:
            print("Retrieved Results", result)
        if args.plot:
            for text_node in result.metadata["text_nodes"]:
                display_source_node(text_node, source_length=4000)
                plot_images([n.metadata["file_path"] for n in result.metadata["image_nodes"]])

    except RuntimeError as e:
        # Check if the error message indicates that the input context is too long
        if 'too long for context length' in str(e):
            result = "No output, likely because the input context is too long"
            if args.verbose: print(result)
        else:
            # If it's a different RuntimeError, raise it
            raise e
    return result


def text_and_all_condition(args, img_from_text_only):
    """
    This function handles cases where the input is text, and the goal is to either:
    1. Extract images embedded within the text context.
    2. Include the extracted images from the text along with their embeddings.

    This function helps manage scenarios where text-based input needs to be augmented with images, 
    either by extracting visual content embedded within the text or by incorporating image embeddings 
    into the processing pipeline.
    """
    retrieval_results, context_str, all_images = retrive_document(args, img_from_text_only=img_from_text_only)
    # GPT_cot (with prompt design)
    prompt_data = get_prompt_by_type(args)
    prompt = prompt_data.format(context_str=context_str, query_str=args.question)
    result = generate_response(args, prompt, all_images)
    return result, retrieval_results

def MMRAG(args):
    if args.retrive:
        result = retrive_document(args, img_from_text_only=False)
        context, scores, context_path = extract_context_and_paths1(result)
        response = ""
    else:
        output = answer_question(args)
        # pdb.set_trace()
        context, scores, context_path = extract_context_and_paths1(output)
        if isinstance(output, str):
            response = output
        else:
            response = output.response
    return [response, context, scores, context_path]

def MMRAG_text(args):
    if args.retrive:
        result = retrive_document(args, img_from_text_only=True)
        context, scores, context_path = extract_context_and_paths1(result)
        response = ""

    else:
        response, retrieval_results = text_and_all_condition(args, img_from_text_only=True)
        context, scores, context_path = extract_context_and_paths2(retrieval_results)

    return [response, context, scores, context_path]

def MMRAG_all(args):
    if args.retrive:
        result = retrive_document(args, img_from_text_only=False)
        context, scores, context_path = extract_context_and_paths1(result)
    else:
        response, retrieval_results = text_and_all_condition(args, img_from_text_only=False)
        context, scores, context_path = extract_context_and_paths2(retrieval_results)
    return [response, context, scores, context_path]