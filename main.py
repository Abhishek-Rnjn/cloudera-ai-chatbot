from fastapi import FastAPI
from Services.Chunker.parserInterface import ParserInterface
from Services.api_caller import predict
app = FastAPI()


@app.get("/")
def health_check():
    predict(input)
    return {"Health": "okay"}


@app.get("/chat")
def chat_with_model(input: str):
    return predict(input)

