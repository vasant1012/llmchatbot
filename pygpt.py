from PyPDF2 import PdfReader
import time
import pickle
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os


class gptbot:   
    os.environ[
        "OPENAI_API_KEY"] = "add ypur openai api key here" 
    
    def __init__(self):
        pass
    
    def chatbot(query, docsearch):
        chain = load_qa_chain(OpenAI(), chain_type="stuff")
        docs = docsearch.similarity_search(query)
        result = chain.run(input_documents=docs, question=query)
        result = result.strip()
        return result
