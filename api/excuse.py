from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Excuse(BaseAPI):
    '''I am my own party.

    excuse: Generates a random excuse.
    excuse for [category]: Generates an excuse for specific category eg, family, office, children, college, party, funny, unbelievable, developers and gaming.'''

    URL = 'https://excuser-three.vercel.app/v1/excuse/'

    def __init__(self) -> None:
        self.categories = (
            'family', 'office', 'children',
            'college', 'party', 'funny',
            'unbelievable', 'developers', 'gaming'
        )

    def validate(self, cmd: Command) -> bool:
        return cmd.command == 'excuse'

    def run(self,  cmd: Command) -> str:
        category = cmd.param.lower()
        if category:
            category = category.split()[-1]
        url = self.URL + category if category in self.categories else self.URL
        return fetch(url, '0.excuse')

    def ping(self) -> bool:
        return bool(fetch(self.URL))
