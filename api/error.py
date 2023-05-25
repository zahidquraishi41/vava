from api.helper.api_base import APIBase
from api.helper.message import Message
import random


class Error(APIBase):

    def __init__(self) -> None:
        self.priority = 4
        self.messages = (
            'Here is a peanut for you! happy now :3',
            '...',
            "I don't wanna",
            'Nope, maybe later',
            'Are you refering to me?',
            "I.. I- I won't",
            'Task failed successfully',
            'An error occured while displaying the previous error',
            "I'm going to walk the dog",
            "I'm not paid enough to do this",
            '*ignores*',
            "The potato server is currently experiencing a mid-life crisis. Please be patient while it figures things out.",
            "I'm sorry, I'm allergic to that command. ",
            "Tsk, you really don't listen, do you? Your command was rejected. Maybe if you asked nicely, I might consider it.",
        )

    def validate(self, msg: Message):
        # There is 5% that it'll be executed on random
        return msg.command == 'error' or \
            random.choices([True, False], [0.05, 0.95], k=1)[0]

    def run(self,  msg: Message):
        return random.choice(self.messages)

    def help(self):
        return {
            'error': 'Generates a random funny message that has nothing to do with error.'
        }
