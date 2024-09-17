from fastapi import FastAPI, Response, Form, Request
from threading import Thread
import ssl
import urllib.request
from fastapi.responses import PlainTextResponse
import threading
from src.Services.driver import Driver
from src.Models.initialize_model import InitializeVectorStore
from src.utils.slack_utils import process_message
from src.Services.api_caller import predict

ssl._create_default_https_context = ssl._create_unverified_context
app = FastAPI()
driver = Driver()  # Initialize the Driver class to interact with the retriever and LLM

@app.post("/ask")
async def handle_slack_command(
    request: Request,
    channel_id: str = Form(...),
    text: str = Form(...),
    user_id: str = Form(...),
):
    # process as need resp in 3 seconds
    response = PlainTextResponse(content="Processing ... ")

    # using thread......... to do things in background
    thread = threading.Thread(target=process_message, args=(channel_id, user_id, text))
    thread.start()

    return response


@app.get("/")
def home_page():
    # Write a beautiful html page to return saying welcome to AI assistant
    return {"message": "Welcome to AI Assistant"}

@app.get("/v1/health")
def health_check():
    return {"status": "OK"}

@app.post("/v1/initialize_application")
def initialize_application(initialize_vector_store: InitializeVectorStore):
    print(initialize_vector_store)
    # Initialize the application with the provided pdf links and google drive link
    # Implement the logic to initialize the application using the provided links
    # need to make this asynchronous and add a status check. @praneet/ @mihir
    driver.initailize_db(initialize_vector_store.pdf_links, initialize_vector_store.google_drive_link)
    return {"message": "Application initialized successfully"}

@app.get("/v1/interact")
def interact_with_model(input: str):
    # Interact with the initialized model using the provided input
    # Implement the logic to interact with the model and return the response
    return driver.render(input)


@app.get("/chat")
def chat_with_model(input: str):
    return predict(input)

