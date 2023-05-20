from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import requests


class Fact(APIBase):

    def validate(self, msg: Message):
        return msg.command == 'fact'

    def run(self,  msg: Message):
        url = 'https://uselessfacts.jsph.pl/random.json?language=en'
        return fetch(url, 'text')

    def help(self):
        return {
            'fact': 'Generates a random useless fact.'
        }
