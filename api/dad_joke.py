from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class DadJoke(BaseAPI):
    """TODO"""

    URL = "https://official-joke-api.appspot.com/jokes/random"

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "dad" and "joke" in cmd.param

    def run(self, cmd: Command) -> str:
        setup, punchline = fetch(self.URL, ["setup", "punchline"])
        return setup + "\n" + punchline

    def ping(self) -> bool:
        return bool(self.run(None))
