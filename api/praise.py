from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import requests


class Praise(APIBase):

    def validate(self, msg: Message):
        return (
            msg.command == 'praise' or
            msg.command.startswith('praise ')
        )

    def run(self,  msg: Message):
        url = 'https://complimentr.com/api'
        name = msg.command.split(' ', 1)[1] if ' ' in msg.command else msg.author
        if name == 'me':
            name = msg.author
        return name + '\n' + fetch(url, 'compliment')

    def help(self):
        return {
            'praise': 'You\'re the best! You deserve a compliment!.'
        }
