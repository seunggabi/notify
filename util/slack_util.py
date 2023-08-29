import logging

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)


def chat(token, channel, text):
    client = WebClient(token=token)

    response = None
    try:
        response = client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        logger.error(f"[Error] posting message: {e}")

    return {
        "channel": channel,
        "text": text,
        "response": response
    }


def files(token, channel, file):
    client = WebClient(token=token)

    response = None
    try:
        response = client.files_upload(
            channels=channel,
            initial_comment=None,
            file=file,
        )
    except SlackApiError as e:
        logger.error(f"[Error] uploading file: {e}")

    return {
        "channel": channel,
        "file": file,
        "response": response
    }
