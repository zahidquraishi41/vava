from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch


class Greet(APIBase):

    def validate(self, msg: Message):
        return all([
            msg.content == 'vava' or
            msg.command == 'greet' or
            msg.command.startswith('greet ')
        ])

    def run(self,  msg: Message):
        url = 'https://www.greetingsapi.com/random'

        name = msg.author
        if msg.command.startswith('greet '):
            name = msg.command[6:]

        return fetch(url, 'greeting') + f' {name}'

    def help(self):
        return {
            'greet': 'Greets the author',
            'greet [NAME]': 'Greets [NAME]'
        }
