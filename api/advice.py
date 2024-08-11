from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Advice(BaseAPI):
    '''Sometimes it's best to ignore other people's advice.
    advice: Retrieves a random advice message.
    advice [name]: Retrieves advice message for [name]'''

    URL = 'https://api.adviceslip.com/advice'

    def validate(self, msg: Command):
        return msg.command == 'advice'

    def run(self,  cmd: Command):
        user = cmd.author if cmd.param == 'me' else cmd.param
        user = user + '\n' if user else user
        return user + fetch(self.URL, 'slip.advice')

    def ping(self) -> bool:
        return bool(fetch(self.URL, 'slip.advice'))
