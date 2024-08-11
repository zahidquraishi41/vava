from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Insult(BaseAPI):
    '''You pusillanimous scoundrel.
    insult: Generates the most evil insults.
    insult [name]: Generates the most evil insults for [name].'''

    URL = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'

    def validate(self, cmd: Command) -> bool:
        return (
            cmd.command == 'insult' or
            cmd.command.startswith('insult ')
        )

    def run(self,  cmd: Command) -> str:
        name = cmd.param
        if name:
            name = cmd.author if cmd.param == 'me' else cmd.param
            name += '\n'
        return name + fetch(self.URL, 'insult')

    def ping(self) -> bool:
        return bool(fetch(self.URL, 'insult'))
