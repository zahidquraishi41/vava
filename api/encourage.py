from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch
import random


class Encourage(BaseAPI):
    '''Success is the progressive realization of a worthy goal.

    encourage: Generates a random encouraging quote.
    encourage [name]: Generates quote encouraging quote for [name].
    '''

    def validate(self, cmd: Command) -> bool:
        return cmd.command == 'encourage'

    def run(self,  cmd: Command) -> str:
        name = cmd.param
        if name:
            name = cmd.author if cmd.param == 'me' else cmd.param
            name += '\n'
        quote = random.choice((self.affirmations, self.zenquotes))()
        return name + quote

    def ping(self) -> bool:
        return all((self.zenquotes(), self.affirmations()))

    @staticmethod
    def zenquotes() -> str:
        url = 'https://zenquotes.io/api/random'
        msg, author = fetch(url, ['0.q', '0.a'])
        return msg + ' -' + author

    @staticmethod
    def affirmations() -> str:
        url = 'https://www.affirmations.dev/'
        return fetch(url, 'affirmation')
