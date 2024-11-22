#RAG.py
import os
from llama_index.llms.openai import OpenAI
import pdb

from utils import get_prompt_by_type, extract_context_and_paths1

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
        print('Rag Prompt:\n')
        # print(prompts_dict['response_synthesizer:text_qa_template'].default_template.template)
        print(prompts_dict['response_synthesizer:text_qa_template'].template)
        print()
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

    

    


