from src.Services.RAG.embedder import CAIIEmbeddings
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from typing import List
import bs4
from langchain_openai import ChatOpenAI

class BasicRetriever:

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
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
        splits = text_splitter.split_documents(docs)
        return splits
    
    def get_retriever(self, splits):
        vectorstore = Chroma.from_documents(documents=splits, 
                                    embedding=CAIIEmbeddings())
        # vectorstore.aadd_documents()
        retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
        return retriever
    
    def add_docs_embeddings_to_db(self, docs: List[Document]) -> bool:
        # implement
        return True

    

if __name__ == "__main__":
    retriever = BasicRetriever()
    links = ["https://docs.cloudera.com/machine-learning/cloud/product/topics/ml-product-overview.html"]
    docs = retriever.web_doc_loader(links)
    #splits = retriever.text_splitter(docs)
    #retriever = retriever.get_retriever(splits)
    #docs = retriever.get_relevant_documents("What is Task Decomposition?")
    print(docs)

