from langchain_core.documents import Document
from typing import List
from src.Services.RAG.retriever import BasicRetriever
from src.Services.Chunker.listGoogleDrive import create_documents
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader


class Parser:
    def __init__(self):
        self.db = BasicRetriever()

    def load_local_file(self, filenames: List[str]) -> bool:
        pages = []
        for file_path in filenames:
            loader = PyPDFLoader(file_path)
            pages.extend(loader.load_and_split())
        return self.db.add_docs_embeddings_to_db(docs=pages)

    def load_files_from_drive(self, filename: List[str]) -> bool:
        #a = Document(page_content= "abc", metadata ={"name": filename})
        docs = create_documents()
        return self.db.add_docs_embeddings_to_db(docs=docs)

    def load_files_from_web(self, links: List[str]) -> bool:
        loader = WebBaseLoader(
            web_paths=(links))
        docs = loader.load()
        return self.db.add_docs_embeddings_to_db(docs=docs)


if __name__ == '__main__':
    #Parser().load_files_from_web(['https://docs.cloudera.com/machine-learning/cloud/product/topics/ml-product-overview.html'])
    Parser().load_files_from_web(['https://docs.cloudera.com/machine-learning/cloud/index.html'])
    #Parser().load_local_file(['Kubernetes.pdf'])
