from src.Services.RAG.embedder import CAIIEmbeddings
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from typing import List
import bs4
from langchain_openai import ChatOpenAI
from src.Services.RAG.CONSTS import PERSIST_DIRECTORY, IDS_PATH
import uuid
import pickle
import os

class BasicRetriever:

    def __init__(self) -> None:
        self.retriever = None

    # this is not problematic
    def web_doc_loader(self, links: List[str]) -> List[Document]:
        loader = WebBaseLoader(
        web_paths=(links),
        # bs_kwargs=dict(
        #     parse_only=bs4.SoupStrainer(
        #         class_=("post-content", "post-title", "post-header")
        #     )
        # ),
    )
        docs = loader.load()
        return docs
    
    # Chunking
    def text_splitter(self, docs: List[Document]) -> List[Document]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        return splits 
    
    def get_seen_ids(self):
        absolute_path = os.path.join(os.getcwd(), IDS_PATH)
        print(f"Absolute path: {absolute_path}")
        if os.path.exists(absolute_path):
            with open(absolute_path, "rb") as f:
                seen_ids = pickle.load(f)
                print(f"Loaded seen ids with length {len(seen_ids)}")
        else:
            print("No seen Ids")
            seen_ids = set()
        return seen_ids
    
    def fetch_latest_retriever(self):
        if self.retriever is None:
            vectorstore = Chroma(embedding_function=CAIIEmbeddings(), persist_directory=PERSIST_DIRECTORY)
            self.retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
        return self.retriever


    def get_retriever(self, docs, initialization: bool = False):
        if initialization:
            ids = [str(uuid.uuid5(uuid.NAMESPACE_DNS, doc.page_content)) for doc in docs]
            unique_ids = list(set(ids))
            # Ensure that only docs that correspond to unique ids are kept and that only one of the duplicate ids is kept
            seen_ids = self.get_seen_ids()
            unique_docs = [doc for doc, id in zip(docs, ids) if id not in seen_ids and (seen_ids.add(id) or True)]
            print(f"Total unique docs: {len(unique_docs)}")
            if len(unique_docs) == 0:
                vectorstore = Chroma(embedding_function=CAIIEmbeddings(), persist_directory=PERSIST_DIRECTORY)
            else:
                vectorstore = Chroma.from_documents(unique_docs,ids= unique_ids,
                                            embedding=CAIIEmbeddings(),
                                            persist_directory=PERSIST_DIRECTORY)
                print("Persisting DB.")
                vectorstore.persist()
            # save the new seen ids
            with open(os.path.join(os.getcwd(), IDS_PATH), "wb") as f:
                pickle.dump(seen_ids, f)
                print("Saved seen ids")
            print("Persisted")
        else:
            vectorstore = Chroma(embedding_function=CAIIEmbeddings(), persist_directory=PERSIST_DIRECTORY)
        # vectorstore.aadd_documents()
        retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
        self.retriever = retriever
        return self.retriever
    
    def add_docs_embeddings_to_db(self, docs: List[Document]) -> bool:
        print("The type of document passed to this function is:- ")
        for doc in docs:
            print(type(doc))
        try:
            docs = self.text_splitter(docs)
            ids = [str(uuid.uuid5(uuid.NAMESPACE_DNS, doc.page_content)) for doc in docs]
            unique_ids = list(set(ids))
            seen_ids = self.get_seen_ids()
            unique_docs = [doc for doc, id in zip(docs, ids) if id not in seen_ids and (seen_ids.add(id) or True)]
            if len(unique_docs) == 0:
                print("No unique documents found.")
                return True
            vectorstore = Chroma(embedding_function=CAIIEmbeddings(), persist_directory=PERSIST_DIRECTORY)
            ids = vectorstore.add_documents(unique_docs, ids= unique_ids)
            print(f"added in the vector store db with total ids {len(ids)}")
            vectorstore.persist()
            print("Persisted the db")
            with open(os.path.join(os.getcwd(), IDS_PATH), "wb") as f:
                pickle.dump(seen_ids, f)
                print("Saved seen ids")
            self.retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
            return True
        except Exception as e:
            print(f"Error while adding docs to db: {e}")
            return False

    

if __name__ == "__main__":
    retriever = BasicRetriever()
    links = ["https://docs.cloudera.com/machine-learning/cloud/product/topics/ml-product-overview.html"]
    docs = retriever.web_doc_loader(links)
    #splits = retriever.text_splitter(docs)
    #retriever = retriever.get_retriever(splits)
    #docs = retriever.get_relevant_documents("What is Task Decomposition?")
    print(docs)

