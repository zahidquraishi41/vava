from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Duck(BaseAPI):
    """TODO"""

    URL = "https://random-d.uk/api/random"

    def __init__(self) -> None:
        super().__init__()
        self.priority = 11

    def validate(self, cmd: Command) -> bool:
        return cmd.command in ("duck", "quake")

    def run(self, cmd: Command | None) -> str:
        return fetch(f"{self.URL}", "url")

    def ping(self) -> bool:
        return bool(self.run(None))
