from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch


class Excuser(APIBase):

    def validate(self, msg: Message):
        return (
            msg.command in ('excuse', 'excuses') or
            msg.command.startswith('excuse ') or
            msg.command.startswith('excuse for ')
        )

    def run(self,  msg: Message):
        url = 'https://excuser-three.vercel.app/v1/excuse'

        category = ''
        if msg.command.startswith('excuse ') or msg.command.startswith('excuse for '):
            category = msg.command.split()[-1]
        if category not in ('family', 'office', 'children', 'college', 'party',
                            'funny', 'unbelievable', 'developers', 'gaming'):
            category = ''
        url += '/' + category

        return fetch(url, '0.excuse')

    def help(self):
        return {
            'excuse':
            'Generates a random excuse.',
            'excuse for [CATEGORY]':
            'Category can be Family, Office, Children, College, Party, Funny, Unbelievable, Developers, Gaming'
        }
