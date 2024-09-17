import os
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/documents.readonly']

def authenticate_google_services(credentials_path):
    """Authenticate and create Google Drive and Docs services."""
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)

    drive_service = build('drive', 'v3', credentials=creds)
    docs_service = build('docs', 'v1', credentials=creds)

    return drive_service, docs_service

def list_all_files(service):
    """List all files in Google Drive."""
    results = service.files().list(
        pageSize=1000,
        fields="nextPageToken, files(id, name, mimeType)",
        q="mimeType='application/vnd.google-apps.document'"
    ).execute()
    return results.get('files', [])

def fetch_google_document(document_id, docs_service):
    """Fetch the content of a Google Document."""
    document = docs_service.documents().get(documentId=document_id).execute()
    text_list = []
    for elem in document.get('body', {}).get('content', []):
        if 'paragraph' in elem:
            for e in elem['paragraph'].get('elements', []):
                if 'textRun' in e and 'content' in e['textRun']:
                    text_list.append(e['textRun']['content'])
    return ''.join(text_list)

def main():
    credentials_path = 'credentials_desktop.json'

    drive_service, docs_service = authenticate_google_services(credentials_path)

    files = list_all_files(drive_service)

    if not files:
        print('No files found.')
    else:
        print('Files:')
        for file in files:
            file_id = file.get('id')
            file_name = file.get('name')
            print(f'File Name: {file_name}, File ID: {file_id}')

            content = fetch_google_document(file_id, docs_service)
            print(f'Content of {file_name}:\n{content}\n')

if __name__ == '__main__':
    main()