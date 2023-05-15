from api.helper.api_base import APIBase
from api.helper.message import Message


class Dad(APIBase):

    def __init__(self) -> None:
        self.enabled = True
        super().__init__(6)

    def validate(self, msg: Message):
        return (
            (msg.command == 'dad enable' or msg.command == 'dad disable') or
            (self.enabled and ("i'm " in msg.msg or 'i am ' in msg.msg))
        )

    def run(self,  msg: Message):
        if msg.command == 'dad enable':
            self.enabled = True
            return
        elif msg.command == 'dad disable':
            self.enabled = False
            return

        if "i'm " in msg.content:
            name = msg.content.split("i'm ", 1)[1]
        else:
            name = msg.content.split("i am ", 1)[1]

        return f'hello {name}, i am vava'

    def help(self):
        return {
            'dad enable': 'Enable this service.',
            'dad disable': 'Disable this service.'
        }
