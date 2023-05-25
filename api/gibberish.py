from api.helper.api_base import APIBase
from api.helper.message import Message
import random
from gibberish import Gibberish as Gib


class Gibberish(APIBase):

    def __init__(self) -> None:
        self.priority = 6

    def validate(self, msg: Message):
        return msg.content.startswith('vava ')

    def run(self,  msg: Message):
        length = random.randint(3, 6)
        gib = ' '.join(Gib().generate_words(length))
        return gib

    def help(self):
        return {
            'gibberish': 'Returns a gibberish message.'
        }
