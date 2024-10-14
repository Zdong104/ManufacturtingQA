#RAG.py
import os
from llama_index.llms.openai import OpenAI

from utils import get_prompt_by_type, extract_context_and_paths1


def load_index_from_storage(args):
    from llama_index.core import StorageContext, load_index_from_storage
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=args.MMVectorDB_path)
    # load index
    index = load_index_from_storage(storage_context)
    args.index = index
    return

def build_index(args):
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
    required_exts = [".txt"]
    documents = SimpleDirectoryReader(args.document,required_exts=required_exts,recursive=True).load_data()
    print(f"Loaded {len(documents)} docs")
    index = VectorStoreIndex.from_documents(documents, chunk_size=args.chunk_size, chunk_overlap=args.chunk_overlap)
    index.storage_context.persist(persist_dir=args.MMVectorDB_path) # Save the index to disk
    args.index = index
    return

def retrive_document(args) -> str:
    retriever = args.index.as_retriever(similarity_top_k=args.top_k)
    if args.interactive:
        args.question = input("Enter your question: ")
    args.results = retriever.retrieve(args.question)
    if args.verbose:
        for result in args.results:
            print("#" * 100)
            print(result.text)
    return args.results

def answer_question(args) -> str:
    from llama_index.core import PromptTemplate
    llm = OpenAI(model=args.model)
    query_engine = args.index.as_query_engine(llm=llm, similarity_top_k=args.top_k)
    new_summary_tmpl = PromptTemplate(get_prompt_by_type(args))
    query_engine.update_prompts({"response_synthesizer:text_qa_template": new_summary_tmpl})
    prompts_dict = query_engine.get_prompts()
    if args.verbose:
        print(prompts_dict['response_synthesizer:text_qa_template'].template)
    args.results = query_engine.query(args.question)
    return args.results

def RAG(args):
    if args.retrive:
        output = retrive_document(args)
        context, scores, context_path = extract_context_and_paths1(output)
        response = ""
    else:
        output = answer_question(args)
        context, scores, context_path = extract_context_and_paths1(output)
        response = output.response
    return [response, context, scores, context_path]

    

    


