from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import requests


class Spam(APIBase):

    def validate(self, msg: Message):
        return (
            msg.command.startswith('spam ') or
            msg.command.startswith('mention ') or
            msg.command.startswith('annoy ')
        )

    def run(self,  msg: Message):
        count = msg.command.split()[-1]
        count = int(count) if count.isdigit() else 5

        if count > 30:
            raise Exception('Mention count exceeds the top limit.')

        if len(msg.message.mentions) == 0:
            raise Exception('No mention found in the message.')

        user = msg.message.mentions[0].mention
        return [user for _ in range(count)]

    def help(self):
        return {
            'spam/annoy/mention [NAME] [COUNT]': 'Mentions [NAME], [COUNT] number of times.'
        }
