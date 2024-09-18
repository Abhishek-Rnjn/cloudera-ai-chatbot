import pickle
import os
from io import BytesIO
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
from langchain_core.documents import Document
from typing import List

#from tabulate import tabulate

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']


def get_gdrive_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # return Google Drive API service
    return build('drive', 'v3', credentials=creds)


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20 MB'
        1253656678 => '1.17 GB'
    """
    units = ["", "KB", "MB", "GB", "TB"]

    if b == 0:
        return f"0{suffix}"

    unit_index = 0
    while b >= factor and unit_index < len(units) - 1:
        b /= factor
        unit_index += 1

    return f"{b:.2f} {units[unit_index]}"


def list_files(items):
    """Given items returned by Google Drive API, prints them in a tabular way."""
    if not items:
        print('No files found.')
        return

    rows = []
    for item in items:
        # print(item)
        id = item.get("id", "N/A")
        name = item.get("name", "N/A")
        parents = ", ".join(item.get("parents", ["N/A"]))
        size = "N/A"

        if "size" in item:
            try:
                size = get_size_format(int(item["size"]))
            except ValueError:
                size = "N/A"

        mime_type = item.get("mimeType", "N/A")
        modified_time = item.get("modifiedTime", "N/A")

        rows.append((id, name, parents, size, mime_type, modified_time))

    print("Files:")
    #table = tabulate(rows, headers=["ID", "Name", "Parents", "Size", "Type", "Modified Time"])
    # print(table)


def create_documents() -> List[Document]:
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 5 files the user has access to.
    """
    service = get_gdrive_service()
    shared_drive_id = '0ADGBOd2_kNY6Uk9PVA'
    folder_id = "1R0PkN4FUqLhbPiyqxg6uTrhR3Dux_EGs"
    query = f"'{folder_id}' in parents"
    # folder_metadata = service.files().get(fileId=folder_id, fields='id, name').execute()
    # print("metadat:", folder_metadata)
    # Call the Drive v3 API
    results = service.files().list(
        q=query,
        spaces='drive',
        corpora='drive',
        driveId=shared_drive_id,
        includeItemsFromAllDrives=True,
        supportsAllDrives=True,
        pageSize=100,
        fields="nextPageToken, files(id, name, mimeType, size, parents, modifiedTime)"
    ).execute()
    # get the results
    all_items = []
    items = results.get('files', [])
    while items:
        all_items.extend(items)
        next_page_token = results.get('nextPageToken')
        if not next_page_token:
            break
        results = service.files().list(
            q=query,
            spaces='drive',
            corpora='drive',
            driveId=shared_drive_id,
            includeItemsFromAllDrives=True,
            supportsAllDrives=True,
            pageSize=50,
            fields="nextPageToken, files(id, name, mimeType, size, parents, modifiedTime)",
            pageToken=next_page_token
        ).execute()
        items = results.get('files', [])
    #list_files(all_items)
    docs = []
    for item in all_items:
        #fileId="1yRpks3-0xJ42fYlr1NJXcM6U2iIPNLg429qVXldzTjY",
        mime_type = item.get("mimeType", "N/A")
        #TODO:Ignore Folders for now
        if mime_type != 'application/vnd.google-apps.document':
            continue
        id = item.get("id", "N/A")
        file_content = service.files().export(
            fileId=id,
            mimeType="text/plain"
        ).execute()
        #print(file_content.decode("utf-8"))
        doc = Document(file_content.decode("utf-8"))
        print(doc.page_content)
        docs.append(doc)
    return docs


if __name__ == '__main__':
    create_documents()
