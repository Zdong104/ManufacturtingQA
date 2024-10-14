# main.py
import argparse
import os
import pandas as pd
# load local function
from utils import generate_response, get_prompt_by_type, data_processor, save_results_to_folder, build_index, load_index_from_storage
from RAG import RAG
from MMRAG import MMRAG, MMRAG_text, MMRAG_all
import pdb

parser = argparse.ArgumentParser()
parser.add_argument("--QAType", default = 4, type = int, help = "Which Type of Question to be asked, we have 1.MCQ, 2.ResponseQ, 3.ImageQ, 4.MathQ")
parser.add_argument("--verbose", default = False, type = bool, help = "Print the output or not")
parser.add_argument("--plot", default = False, type = bool, help = "Plot the output or not")
parser.add_argument("--evidence", default = False, type = bool, help = "Print and Plot the source of the answer")
parser.add_argument("--api_key", default=os.getenv("OPENAI_API_KEY"), type=str, help="OpenAI API Key")
parser.add_argument("--top_k", default = 3, type = int, help = "Top k answer to be generated")
parser.add_argument("--image_top_k", default = 3, type = int, help = "Top k image to be generated")
parser.add_argument("--retrive", default = False, type = bool, help = "Retrive the document or answer_question, depend on if want to test or question answering")
parser.add_argument("--interactive", default = False, type = bool, help = "User can input the question, or use default question where can be deined below")
parser.add_argument("--model", default = "gpt-4o", type = str, help = "The model to be used, right now we only support gpt-4o")
# if rebuild index, define the following
parser.add_argument("--rebuild_index", default = False, type = bool, help = "Rebuild the index or not")
parser.add_argument("--document", default = "1Book/3Book_txt_images", type = str, help = "The document (Book) to be used")
parser.add_argument("--chunk_size", default = 600, type = int, help = "The chunk size of the document")
parser.add_argument("--chunk_overlap", default = 100, type = int, help = "The chunk overlap of the document")
args = parser.parse_args()
print(args)
print()
print()


# Function to load all .csv files from a folder into a single dataframe
def load_csv_files_from_folder(folder_path):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # Load all CSVs into dataframes
    dfs = [pd.read_csv(os.path.join(folder_path, f), header=0) for f in csv_files]
    
    if dfs:
        args.questions_df = pd.concat(dfs, ignore_index=True)  # Concatenate into one dataframe
        
        return args
    else:
        raise ValueError(f"No CSV files found in folder: {folder_path}")

def experiment(args):
    os.environ["OPENAI_API_KEY"] = args.api_key
    GPT_results = []
    GPT_cot_results = []
    RAG_results = []
    MMRAG_results = []
    MMRAG_text_results = []
    MMRAG_all_results = []
    
    if args.rebuild_index:
        build_index(args)
    else:
        load_index_from_storage(args)

    for question in args.questions_df['Question']:
        # GPT (no prompt design)
        GPT_result = generate_response(args, question, image_paths=[])
        
        # GPT_cot (with prompt design)
        prompt_data = get_prompt_by_type(args)
        if prompt_data:
            prompt = prompt_data.format(context_str="", query_str=question)
        else:
            raise ValueError(f"No prompt found for type: {args.QAType}")
        
        GPT_cot_result = generate_response(args, prompt, image_paths=[])
        # RAG and other result types
        args.question = question
        RAG_result = RAG(args)

        MMRAG_result = MMRAG(args)
        MMRAG_text_result = MMRAG_text(args)
        MMRAG_all_result = MMRAG_all(args)

        # Append results to args
        GPT_results.append(GPT_result)
        GPT_cot_results.append(GPT_cot_result)
        RAG_results.append(RAG_result)
        MMRAG_results.append(MMRAG_result)
        MMRAG_text_results.append(MMRAG_text_result)
        MMRAG_all_results.append(MMRAG_all_result)

  

    # Define a dictionary to loop over results and process/save them
    results_mapping = {
        "GPT_results": GPT_results,
        "GPT_cot_results": GPT_cot_results,
        "RAG_results": RAG_results,
        "MMRAG_results": MMRAG_results,
        "MMRAG_text_results": MMRAG_text_results,
        "MMRAG_all_results": MMRAG_all_results
    }
    
    # Process and save each result type
    for result_type, result_list in results_mapping.items(): 
        results_df = data_processor(result_type, result_list, args)
        save_results_to_folder(results_df, args, result_type)

if __name__ == "__main__":
    os.chdir("../../") # change to main directory
    # Set VectorDB path
    args.MMVectorDB_path = "1Book/4.High_Quality_WholeBook_storage"
    # list of all question folders
    RQfolder = "2QuestionsData/1RQ/"
    MCQfolder = "2QuestionsData/2MCQ/"
    ImgQfolder = "2QuestionsData/3ImgQ/"
    MathQfolder = "2QuestionsData/4MathQ/"
    if args.QAType == 1:
        load_csv_files_from_folder(MCQfolder)    
    elif args.QAType == 2:
        load_csv_files_from_folder(RQfolder)
    elif args.QAType == 3:
        load_csv_files_from_folder(ImgQfolder)
    elif args.QAType == 4:
        load_csv_files_from_folder(MathQfolder)
    else:
        raise ValueError("Invalid QAType. Please specify a valid QAType from 1 to 4.")
    args.questions_df = args.questions_df[:3]

    experiment(args)


