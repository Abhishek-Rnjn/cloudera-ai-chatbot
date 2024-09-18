from fastapi import FastAPI, Response, Form, Request, UploadFile, File, HTTPException
from threading import Thread
import ssl
import urllib.request
from fastapi.responses import PlainTextResponse
import threading
from src.Services.driver import Driver
from src.Models.initialize_model import InitializeVectorStore
from src.utils.slack_utils import process_message
from src.Services.api_caller import predict
from typing import List

ssl._create_default_https_context = ssl._create_unverified_context
app = FastAPI()
driver = Driver()  # Initialize the Driver class to interact with the retriever and LLM


@app.post("/ask")
async def handle_slack_command(
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
    return {"message": "Welcome to AI Assistant"}


@app.get("/v1/health")
def health_check():
    return {"status": "OK"}


@app.post("/v1/initialize_application")
def initialize_application(initialize_vector_store: InitializeVectorStore):
    print(initialize_vector_store)
    try:
        driver.initailize_db(initialize_vector_store.pdf_links, initialize_vector_store.google_drive_link)
        return {"message": "Application initialized successfully"}
    except Exception as e:
        raise HTTPException(400, {"message": f"Error initializing application: {str(e)}"})


@app.post("/v1/upload_file")
def upload_pdf(file: UploadFile = File(...)):
    result = driver.store_pdf([file])
    if result:
        return {"message": "File added successfully"}
    else:
        raise HTTPException(400, {"message": "Error adding file"})


@app.post("/v1/add_web_pages")
def add_web_pages(web_pages: List[str]):
    result = driver.parse_web_pages(web_pages)
    if result:
        return {"message": "Web Page added successfully"}
    else:
        raise HTTPException(400, {"message": "Error adding web page"})


@app.post("/v1/add_drive_links")
def add_drive_links(drive_id: str, folders: List[str]):
    result = driver.store_drive_files(folders)
    if result:
        return {"message": "Docs in Drive added successfully"}
    else:
        raise HTTPException(400, {"message": "Error adding Docs present in drive"})


@app.get("/v1/interact")
def interact_with_model(input: str):
    return driver.render(input)


@app.get("/chat")
def chat_with_model(input: str):
    return predict(input)
