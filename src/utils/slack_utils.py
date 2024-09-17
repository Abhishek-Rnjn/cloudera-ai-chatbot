from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from src.Services.api_caller import predict
from utils.CONSTS import SLACK_TOKEN, SLACK_SIGNING_SECRET
slack_token = SLACK_TOKEN
client = WebClient(token=SLACK_TOKEN)

def process_message(channel_id: str, user_id: str, text: str):
    try:
        client.chat_postEphemeral(
            channel=channel_id,
            user=user_id,
            text=f"*`Question`*: {text}"
        )
        response = predict(text)
        print(response)

        message_content = response.choices[0].message.content
        print(message_content)
        client.chat_postEphemeral(
            channel=channel_id,
            user=user_id,
            text=message_content
        )
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")
