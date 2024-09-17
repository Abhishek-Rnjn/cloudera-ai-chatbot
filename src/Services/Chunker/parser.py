from langchain_core.documents import Document
from typing import List
from src.Services.RAG.retriever import BasicRetriever

class Parser:
    def __init__(self):
        self.db = BasicRetriever()

    def load_local_file(self, filename: List[str]) -> List[Document]:
        a = Document(page_content= "abc", metadata ={"name": filename})

        self.db.add_docs_embeddings_to_db([a])
        return a
    
    def load_files_from_drive(self, filename: List[str]) -> List[Document]:
        #self.db.add_docs_embeddings_to_db([a])
        pass

    def load_files_from_web(self, links: List[str]) -> List[Document]:
        #self.db.add_docs_embeddings_to_db([a])
        pass