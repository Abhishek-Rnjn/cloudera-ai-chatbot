from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from src.Services.api_caller import predict
from utils.CONSTS import SLACK_KEY
from src.Services.driver import Driver
driver=Driver()
slack_token = SLACK_KEY
client = WebClient(token=SLACK_KEY)

def process_message(channel_id: str, user_id: str, text: str):
    try:
        client.chat_postEphemeral(
            channel=channel_id,
            user=user_id,
            text=f"*`Question`*: {text}"
        )
        msg_response = driver.render(text)
        print(msg_response)
        client.chat_postEphemeral(
            channel=channel_id,
            user=user_id,
            text=msg_response
        )
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")
