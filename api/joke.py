from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import random
import requests


class Joke(APIBase):

    def validate(self, msg: Message):
        return msg == 'joke'

    def run(self,  msg: Message):
        return random.choice((self.dad_jokes, self.jokes_v2))()

    def help(self):
        return {
            'joke': 'Generates a random joke, sometimes funny.'
        }

    @staticmethod
    def dad_jokes() -> str:
        '''Generates random joke from icanhazdadjoke.com'''
        url = 'https://icanhazdadjoke.com/'
        response = requests.get(url, headers={'Accept': 'text/plain'})
        return response.text

    @staticmethod
    def jokes_v2() -> str:
        '''Generates random joke from v2.jokeapi.dev'''
        url = 'https://v2.jokeapi.dev/joke/Any?safe-mode'
        json_data = fetch(url)
        type = json_data['type']
        if type == 'twopart':
            msg = json_data['setup'] + '\n' + json_data['delivery']
        else:
            msg = json_data['joke']
        return msg
