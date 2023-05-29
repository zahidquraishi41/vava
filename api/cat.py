from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch


class Cat(APIBase):

    def validate(self, msg: Message):
        return msg.command == 'cat'

    def run(self,  msg: Message):
        url = 'https://api.nekos.dev/api/v3/text/cat_emote/'
        return fetch(url, 'data.response.text')

    def help(self):
        return {
            'cat': 'Generates a cat emote.'
        }
