from llama_index.readers.google import GoogleDriveReader
import logging
import sys
import os
from dotenv import load_dotenv
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
LLAMA_CLOUD_API_KEY = "lx-diyfyTqzC3G46rc8LLywzn7UfoFBJQIBlht6UyBnfgH3dFH1"
#load_dotenv()

pdfparser = LlamaParse(api_key= LLAMA_CLOUD_API_KEY, result_type="markdown")
file_extractor = {".pdf": pdfparser}
googleDriveLoader = GoogleDriveReader()

class ParserInterface:
    def parseSingleDoc(self):
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
        filePath = os.path.join(os.getcwd(), 'temp_files/processed_chunks/Kubernetes.pdf')
        print(filePath)
        documents = SimpleDirectoryReader(input_files=[filePath], file_extractor=file_extractor).load_data()
        documents.append(googleDriveLoader.load_data(file_ids=["1KLmtJT7_pWwSykW8J0Dl3foyGI7RkXEoAYsG08siNGw"]))
        print(documents[0].doc_id)
        return documents[0].doc_id
    
    def convertParsedStringJsonl():
        pass