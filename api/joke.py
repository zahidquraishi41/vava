from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch
import random


class Joke(BaseAPI):
    """I asked the surgeon if I could administer my own anesthetic, they said: go ahead, knock yourself out.
    joke: Generates a random joke, sometimes funny."""

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "joke"

    def run(self, cmd: Command) -> str:
        return random.choice((self.dad_jokes, self.jokes_v2))()

    def ping(self) -> bool:
        return bool(self.dad_jokes()) or bool(self.jokes_v2())

    @staticmethod
    def dad_jokes() -> str:
        """Generates random joke from icanhazdadjoke.com"""
        url = "https://icanhazdadjoke.com/"
        return fetch(url, "joke", {"Accept": "application/json"})

    @staticmethod
    def jokes_v2() -> str:
        """Generates random joke from v2.jokeapi.dev"""
        url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
        json_data = fetch(url)
        type = json_data["type"]
        if type == "twopart":
            msg = json_data["setup"] + "\n" + json_data["delivery"]
        else:
            msg = json_data["joke"]
        return msg
