from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from typing import List
from src.Services.RAG.retriever import BasicRetriever
from src.Services.RAG.custom_llm import CustomOpenAIWrapper


class Driver:
    def __init__(self):
        self.retriever =None
        self.llm = None

    
    def initailize_db(self, links : List[str], drive_link = None) -> None:
        links = [l for l in links if l != "string"]
        print(f"The links are \n{links}\n")
        retriever = BasicRetriever()
        docs = retriever.web_doc_loader(links)
        splits = retriever.text_splitter(docs)
        self.retriever = retriever.get_retriever(splits)
        self.llm = CustomOpenAIWrapper()


    def render(self, question):
        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        """

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
