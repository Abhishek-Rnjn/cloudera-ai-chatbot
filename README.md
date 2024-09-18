# Cloudera Intelligent Assistant (CIA) Slack Chat Bot

The **Cloudera Intelligent Assistant (CIA)** is a Slack-integrated chatbot designed to streamline data collection, facilitate intelligent conversations, and interact with external sources like web links, file uploads, and Google Drive. This tool allows users to perform functions like collecting documents, interacting with users via Slack commands, and providing intelligent responses from a model based on user inputs.

## Features

- **Slack Command Handling**: Interact with the bot via Slack by asking questions or uploading data.
- **Data Collection**: Collect data from web pages, file uploads (PDFs), and Google Drive.
- **Model Interaction**: Ask questions and receive intelligent responses based on processed data.
- **Health Check**: Monitor the application status with a health check endpoint.
- **Initialization**: Initialize or reset the application through the initialization API.

---

## API Endpoints

### 1. **POST `/ask` - Handle Slack Command**
   - **Description**: Handles a Slack command from the user. Users can ask a question or give a command, and the bot returns an intelligent response.
   - **Parameters**:
     - `channel_id`: The Slack channel ID.
     - `text`: The user's query or command.
     - `user_id`: The Slack user ID.
   - **Response**: Returns "Processing..." while working on the response.

### 2. **GET `/` - Home Page**
   - **Description**: The home page of the Cloudera Intelligent Assistant. Simple webpage indicating the bot's availability.
   - **Response**: Basic status message.

### 3. **GET `/v1/health` - Health Check**
   - **Description**: Endpoint to check the health of the CIA bot.
   - **Response**: Returns `{"Health": "okay"}` if the application is running correctly.

### 4. **POST `/v1/initialize_application` - Initialize Application**
   - **Description**: Initializes or resets the application, reloading settings or starting a fresh session.
   - **Response**: Confirms successful initialization.

### 5. **POST `/v1/upload_file` - Upload PDF**
   - **Description**: Allows users to upload PDF files for processing.
   - **Request Body**: The PDF file.
   - **Response**: Confirms successful upload and starts processing the content.

### 6. **POST `/v1/add_web_pages` - Add Web Pages**
   - **Description**: Collects data from web page links provided by the user.
   - **Request Body**: 
     - `urls`: A list of web URLs to collect data from.
   - **Response**: Confirms that the web pages have been added and are being processed.

### 7. **POST `/v1/add_drive_links` - Add Drive Links**
   - **Description**: Collects data from Google Drive links.
   - **Request Body**:
     - `drive_links`: A list of Google Drive document or folder links.
   - **Response**: Confirms that the Drive links have been added and content is being retrieved.

### 8. **GET `/v1/interact` - Interact With Model**
   - **Description**: Allows users to directly interact with the AI model. Users can input a query, and the model responds based on the processed data.
   - **Parameters**: 
     - `input`: The query you wish to ask the model.
   - **Response**: Returns the response from the model.

### 9. **GET `/chat` - Chat With Model**
   - **Description**: Simplified interface for chatting with the model. Submit a question or query, and receive a response from the AI model.
   - **Parameters**:
     - `input`: The user's query.
   - **Response**: Returns the response from the model.

---

## How It Works

1. **Slack Integration**: 
   - Users interact with the CIA bot through Slack commands (e.g., `/ask <question>`). The bot processes the command and responds.
   
2. **Data Collection**: 
   - Collects data from web pages, PDF uploads, and Google Drive files. This data is then used by the AI model to respond to queries.
   
3. **Model Interaction**: 
   - The AI model uses the processed data to provide intelligent responses to user queries via Slack or API calls.

---

## Setup and Deployment

### Prerequisites

- Python 3.x
- Slack Bot token and signing secret
- Google API credentials for accessing Google Drive

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd cloudera-ai-chatbot
2. **Install dependencies:**:

   ```bash
   pip install -r requirements.txt
   
3. **Set Up Environment Variables**:

You need to configure environment variables for Slack and Google Drive integration:

- `SLACK_TOKEN`: Your Slack bot token.
  - `SLACK_SIGNING_SECRET`: Your Slack app's signing secret.
  - `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Google API credentials JSON file.

For example, in Linux/Mac, you can add them to your shell configuration:

```bash
export SLACK_TOKEN="your-slack-token"
export SLACK_SIGNING_SECRET="your-slack-signing-secret"
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/google-credentials.json"
```
4. **Set Up Environment Variables**:
   ```bash
   uvicorn app:app --reload

## Usage Examples

### Example Slack Command

You can interact with the CIA bot through Slack by typing:

    ```bash
    /ask What is the content of the uploaded PDF?
The bot will respond with the processed content of the PDF.

## Slack App Configuration

### Create a Slack App

1. Navigate to the [Slack API dashboard](https://api.slack.com/apps) and create a new app.
2. Set up the bot token and add the required OAuth scopes, such as:
   - `chat:write`
   - `files:read`
   - (Add any other necessary scopes based on your requirements)

### Set Up Event Subscriptions

1. Enable Event Subscriptions in your Slack app settings.
2. Provide the bot's public URL for handling events.

### Set Up Slash Commands

1. Create a new slash command (e.g., `/ask`) in the Slack app configuration.
2. Set the request URL to point to your FastAPI endpoint that handles Slack commands.

## Google Drive Integration

To integrate with Google Drive, follow these steps:

### Create Google API Credentials

1. Go to the [Google Developer Console](https://console.developers.google.com/).
2. Create a new project.
3. Enable the Google Drive API for your project.
4. Generate OAuth credentials and download the `client_secrets.json` file.

### Set Up Authentication

1. Place the `client_secrets.json` file on your server.
2. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the credentials file.

