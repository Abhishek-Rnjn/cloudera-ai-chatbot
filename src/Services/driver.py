from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from typing import List
from src.Services.RAG.retriever import BasicRetriever
from src.Services.RAG.custom_llm import CustomOpenAIWrapper
from langchain_core.documents import Document
from src.Services.Chunker.parser import Parser
import shutil
import tempfile
from pathlib import Path
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from src.Services.api_caller import predict
from utils.CONSTS import SLACK_KEY
from src.Services.api_caller import predict
from src.Services.RAG.CONSTS import DEFAULT_FILE

retriever = BasicRetriever()

class Driver:
    def __init__(self):
        self.retriever =None
        self.llm = CustomOpenAIWrapper()
        self.parser = Parser()
        self.__initialized = False


    def initailize_db(self, links : List[str], drive_link = None) -> None:
        if self.__initialized is True:
            raise Exception("Driver is already initialized, Please upload new docs using the upload APIs")
        links = [l for l in links if l != "string"]
        if len(links) == 0:
            links = [DEFAULT_FILE]
        print(f"The links are \n{links}\n")
        docs = retriever.web_doc_loader(links)
        splits = retriever.text_splitter(docs)
        self.retriever = retriever.get_retriever(splits, True)
        self.__initialized = True

    def store_pdf(self, file):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = Path(temp_dir) / file.filename

            # Write the uploaded file to the temporary directory
            with temp_file_path.open("wb") as temp_file:
                shutil.copyfileobj(file.file, temp_file)

            # Return the temporary file path (or you can return a download link if serving the file)
            print(str(temp_file_path))
            return [str(temp_file_path)]
    def add_pdf_db(self, pdf_paths: List[str]) -> bool: #Manas
        # add logic of storing tmp files.

        list_docs = self.parser.load_local_file(pdf_paths)
        self.add_docs_to_db(list_docs)
        return True
        


    def add_docs_to_db(self, docs: List[Document]):  #abhishek
        # self.retriever.add_documents(List[Document])
        pass



    def render(self, question):
        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        """
        self.retriever = retriever.fetch_latest_retriever()
        prompt = ChatPromptTemplate.from_template(template)
        print(f"The prompt template is {prompt}")
        chain = {"context": self.retriever, "question": RunnablePassthrough()} | prompt | self.llm | StrOutputParser()
        print(chain)
        out = chain.invoke(question)
        print(f"out is \n{out}\n")
        return out


if __name__ == "__main__":
    links = ["https://lilianweng.github.io/posts/2023-06-23-agent/"]
    driver = Driver()
    driver.initailize_db(links)
    driver.render("What is Task Decomposition?")
