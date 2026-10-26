from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Fox(BaseAPI):
    """Fox Oxf Xfo"""

    URL = "https://randomfox.ca/floof/"

    def __init__(self) -> None:
        super().__init__()
        self.priority = 11

    def validate(self, cmd: Command) -> bool:
        return cmd.command in ("fox", "floof")

    def run(self, cmd: Command | None) -> str:
        return fetch(self.URL, "image")

    def ping(self) -> bool:
        return bool(self.run(None))
