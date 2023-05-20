from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch, is_similar


class Riddle(APIBase):

    def __init__(self) -> None:
        self.answer = ''

    def validate(self, msg: Message):
        return (
            is_similar(msg.content, self.answer) or
            msg.command == 'riddle' or
            msg.command == 'idk'
        )

    def run(self,  msg: Message):
        if msg.command == 'riddle':
            return self.get_riddle()
        answer = self.answer
        self.answer = ''
        return answer

    def help(self):
        return {
            'riddle': 'Generates a riddle',
            'idk': 'Writes answer for last riddle'
        }

    def get_riddle(self):
        url = 'https://riddles-api.vercel.app/random'
        riddle, answer = fetch(url, ['riddle', 'answer'])
        self.answer = answer.lower()
        return riddle
