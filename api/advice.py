from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import requests


class Advice(APIBase):

    def validate(self, msg: Message):
        return msg.command == 'advice' or msg.command.startswith('advice ')

    def run(self,  msg: Message):
        url = 'https://api.adviceslip.com/advice'
        name = msg.command.split(' ', 1)[1] if ' ' in msg.command else msg.author
        if name == 'me':
            name = msg.author
        return name + '\n' + fetch(url, 'slip.advice')

    def help(self):
        return {
            'advice': 'Gives an advice.'
        }
