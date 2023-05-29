from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch


class Flirt(APIBase):

    def validate(self, msg: Message):
        return (
            msg.command in ('flirt', 'pickup line') or
            msg.command.startswith('flirt ') or
            msg.command.startswith('flirt with ') or
            msg.command.startswith('pickup line for ')
        )

    def run(self,  msg: Message):
        url = 'https://vinuxd.vercel.app/api/pickup'

        # extracting username
        username = msg.author
        if msg.command.startswith('flirt '):
            username = msg.command.split(' ', 1)[1]
        if msg.command.startswith('flirt with '):
            username = msg.command.split(' ', 2)[2]
        if msg.command.startswith('pickup line for '):
            username = msg.command.split(' ', 3)[3]

        return username + '\n' + fetch(url, 'pickup')

    def help(self):
        return {
            'flirt | pickup line': 'Generates pickup line for author',
            'flirt with [NAME]': 'Generates pickup line for [NAME]',
            'pickup line for [NAME]': 'Generates pickup line for [NAME]'
        }
