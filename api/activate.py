from api.helper.api_base import APIBase
from api.helper.message import Message
from api.greet import Greet


class Activate(APIBase):

    def __init__(self) -> None:
        self.priority = 1
        self.active = True

    def validate(self, msg: Message):
        return (
            not self.active or
            msg.command in ('deactivate', 'msg') or
            msg.command in ('activate', 'start')
        )

    def run(self,  msg: Message):
        if not self.active and msg.command not in ('deactivate', 'stop', 'activate', 'start'):
            return

        if not msg.is_admin:
            raise Exception('Requires admin privilege.')

        if msg.command in ('activate', 'listen'):
            msg.command = 'greet ' + msg.author
            out = Greet().execute(msg)
            self.active = True
        else:
            out = f'shutting down AGAIN...' if not self.active else 'shutting down...'
            self.active = False

        return out

    def help(self):
        return {
            'activate/start': 'Activates vava.',
            'deactivate/shutdown': 'Deactivates vava.'
        }
