from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Fact(BaseAPI):
    '''The longest place-name still in use is: Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiakitnatahu, a New Zealand hill.
    fact: Display a random fact.'''

    URL = 'https://uselessfacts.jsph.pl/random.json?language=en'

    def validate(self, cmd: Command) -> bool:
        return cmd.command == 'fact'

    def run(self,  cmd: Command) -> str:
        return fetch(self.URL, 'text')

    def ping(self) -> str:
        return bool(self.run(None))
