import random

from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class XKCD(BaseAPI):
    """TODO"""

    def __init__(self) -> None:
        super().__init__()
        self.priority = 11

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "xkcd"

    def run(self, cmd: Command | None) -> str:
        return fetch(self.get_random_url(), "img")

    def ping(self) -> bool:
        return bool(self.run(None))

    def get_random_url(self):
        num = random.randint(1, 3315)
        while num == 404:
            num = random.randint(1, 3315)
        return f"https://xkcd.com/{num}/info.0.json"
