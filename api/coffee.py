from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Coffee(BaseAPI):
    """TODO"""

    URL = "https://coffee.alexflipnote.dev/random.json"

    def __init__(self) -> None:
        super().__init__()
        self.priority = 11

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "coffee"

    def run(self, cmd: Command | None) -> str:
        return fetch(self.URL, "file")

    def ping(self) -> bool:
        return bool(self.run(None))
