from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = "./assets/AI Engineer.pdf"
loader = PyPDFLoader(file_path, mode="single")

docs = loader.load()

def get_data_from_pdf():

    document_loader = PyPDFLoader(file_path)
    documents = document_loader.load()
    splitter = RecursiveCharacterTextSplitter()
    split_docs = splitter.split_documents(documents)

    for doc in split_docs:
        # print(doc, end="\n")
        if "founded" in doc.page_content.lower():
            doc.metadata['relevance'] = 'founding_date'
        elif "offers" in doc.page_content.lower():
            doc.metadata['relevance'] = 'services_offered'
        else:
            doc.metadata['relevance'] = 'general_info'

    return split_docs
