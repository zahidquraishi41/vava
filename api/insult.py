from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch


class Insult(APIBase):

    def validate(self, msg: Message):
        return msg.command == 'insult' or msg.command.startswith('insult ')

    def run(self,  msg: Message):
        url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
        name = ''

        if ' ' in msg.command:
            name = msg.command.split(' ', 1)[1]
            name += '\n'

        return name + fetch(url, 'insult')

    def help(self):
        return {
            'insult': 'Detailed insults'
        }
