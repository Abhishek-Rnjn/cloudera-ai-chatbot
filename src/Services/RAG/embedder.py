from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings
from typing import List
import requests
import json
from src.Services.RAG.CONSTS import EMBEDDING_ENDPOINT, OPENAI_API_KEY

class CAIIEmbeddings(Embeddings):
    def __init__(self):
        self.url = EMBEDDING_ENDPOINT
        self.headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
        }

    def get_embeddings(self, sentences):
        print(f"The length of sentences is {len(sentences)}")
        if len(sentences) == 0:
            return []
        payload = json.dumps({
            "input": sentences,
            "model": "snowflake/arctic-embed-l",
            "input_type": "query"
            })
        response = requests.request("POST", self.url, headers=self.headers, data=payload, verify=False)
        data = response.json()['data']
        all_embeddings = [0] * len(sentences)
        for embedding in data:
            all_embeddings[embedding['index']] = embedding['embedding']
        print(f"The total embeddings are {len(all_embeddings)}")
        return all_embeddings 

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.get_embeddings(texts)
    
    def embed_query(self, query: str) -> List[float]:
        return self.get_embeddings([query])[0]


if __name__ == "__main__":
    a = CAIIEmbeddings()
    print(a.embed_query("test"))

