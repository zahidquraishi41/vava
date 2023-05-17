from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import urllib


class Quote(APIBase):

    def validate(self, msg: Message):
        return (
            msg.command == 'quote' or
            msg.command.startswith('quote from ') or
            msg.command.startswith('quote by ')
        )

    def run(self,  msg: Message):
        if ' ' in msg.command:
            name = msg.command.split(' ', 2)[-1]
            name = urllib.parse.quote(name)

        query = ''
        if msg.command.startswith('quote from '):
            query = f"/anime?title={name}"
        if msg.command.startswith('quote by '):
            query = f"/character?name={name}"

        url = f'https://animechan.vercel.app/api/random{query}'
        quote, character, anime = fetch(url, ['quote', 'character', 'anime'])

        return f'{quote} -{character} ({anime})'

    def help(self):
        return {
            'quote': 'Generates a random anime quote',
            'quote from [ANIME]': 'Generates random quote from [ANIME]',
            'quote by [CHARACTER]': 'Generates random quote by [CHARACTER]'
        }
