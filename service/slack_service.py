import os
import requests
from PIL import Image
from config import SLACK
from service import MessageService
from util import slack_util
from util.core_util import line_break
from util.date_util import timestamp

CHUNK = 35000


class SlackService:
    def __init__(self):
        pass

    @staticmethod
    def send(message, token, channel, image, test):
        if token is None:
            token = SLACK["TOKEN"]
        if test is None:
            test = False
        if channel is None:
            channel = (
                SLACK["CHANNEL_TEST"] if str(test).lower() == "true" else SLACK["CHANNEL"]
            )

        message = line_break(message)
        if message:
            for m in MessageService(message, step=CHUNK):
                slack_util.chat(token, channel, m)

        if image:
            if isinstance(image, str):
                f = Image.open(requests.get(image, stream=True).raw)
                file = timestamp() + ".png"
                f.save(file)

                slack_util.files(token, channel, file)

                os.remove(file)

        return {
            "message": message,
            "image": image
        }
