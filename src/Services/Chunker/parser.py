from langchain_core.documents import Document
from typing import List
#from src.Services.RAG.retriever import BasicRetriever
from listGoogleDrive import create_documents
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader


class Parser:
    #def __init__(self):
        #self.db = BasicRetriever()

    def load_local_file(self, filename: List[str]) -> List[Document]:
        a = Document(page_content= "abc", metadata ={"name": filename})
        file_path = filename[0]
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        self.db.add_docs_embeddings_to_db(docs=pages)
        return pages
    
    def load_files_from_drive(self, filename: List[str]) -> List[Document]:
        #a = Document(page_content= "abc", metadata ={"name": filename})
        docs = create_documents()
        self.db.add_docs_embeddings_to_db(docs=docs)
        return docs

    def load_files_from_web(self, links: List[str]) -> List[Document]:
        loader = WebBaseLoader(
        web_paths=(links))
        docs = loader.load()
        self.db.add_docs_embeddings_to_db(docs=docs)
        return docs
                

if __name__ == '__main__':
    Parser().load_files_from_web(['https://docs.cloudera.com/machine-learning/cloud/product/topics/ml-product-overview.html'])
    #Parser().load_files_from_web(['https://docs.cloudera.com/machine-learning/cloud/index.html'])
    #Parser().load_local_file(['Kubernetes.pdf'])