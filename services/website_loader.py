import os
# Configura un nombre descriptivo para tu bot
os.environ["USER_AGENT"] = "PromtiorBot/1.0 (Chatbot Challenge Project)"

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_data_from_website(url):

    loader = WebBaseLoader(url)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter()


    return splitter.split_documents(docs)

