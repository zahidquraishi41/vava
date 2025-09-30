from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Rizz(BaseAPI):
    """Sorry, but you owe me a drink. [Why?] Because when I looked at you, I dropped mine.
    rizz: Generates a random pickup line.
    rizz [name]: Generates pickup line for [name]."""

    URL = "https://rizzapi.vercel.app/random"

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "rizz" or cmd.command.startswith("rizz ")

    def run(self, cmd: Command) -> str:
        name = cmd.param
        if name:
            name = cmd.author if cmd.param == "me" else cmd.param
            name += "\n"
        return name + fetch(self.URL, "text")

    def ping(self) -> bool:
        return bool(fetch(self.URL, "text"))
