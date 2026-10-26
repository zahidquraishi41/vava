from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Woof(BaseAPI):
    """Woof Oofw Ofwo Fwoo"""

    URL = "https://random.dog/woof.json"

    def __init__(self) -> None:
        super().__init__()
        self.priority = 11

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "woof"

    def run(self, cmd: Command | None) -> str:
        return fetch(self.URL, "url")

    def ping(self) -> bool:
        return bool(self.run(None))
