from embedder import CAIIEmbeddings
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from typing import List
import bs4
from langchain_openai import ChatOpenAI

class BasicRag:

    def web_doc_loader(self,links: List[str]) -> List[Document]:
        loader = WebBaseLoader(
        web_paths=(links),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
        docs = loader.load()
        return docs
    
    def text_splitter(self, docs: List[Document]) -> List[Document]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        return splits
    
    def get_retriever(self, splits):
        vectorstore = Chroma.from_documents(documents=splits, 
                                    embedding=CAIIEmbeddings())

        retriever = vectorstore.as_retriever()
        return retriever
    



