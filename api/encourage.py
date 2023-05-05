from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import random


class Encourage(APIBase):

    def validate(self, msg: Message):
        return msg.command == 'encourage' or msg.command.startswith('encourage ')

    def run(self,  msg: Message):
        name = msg.command.split(' ', 1)[1] \
            if ' ' in msg.command else msg.author
        if name == 'me':
            name = msg.author
        quote = random.choice((self.affirmations, self.zenquotes))()
        return name + '\n' + quote

    def help(self):
        return {
            'encourage': 'Generates a random encouraging quote.',
            'encourage [NAME]': 'Greets [Name] then generates quote encouraging quote.'
        }

    @staticmethod
    def zenquotes() -> str:
        url = 'https://zenquotes.io/api/random'
        msg, author = fetch(url, ['0.q', '0.a'])
        return msg + ' -' + author

    @staticmethod
    def affirmations() -> str:
        url = 'https://www.affirmations.dev/'
        return fetch(url, 'affirmation')
