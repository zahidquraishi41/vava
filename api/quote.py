from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Quote(BaseAPI):
    """TODO"""

    URL = "https://api.animechan.io/v1/quotes/random"

    def __init__(self) -> None:
        super().__init__()

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "quote"

    def run(self, cmd: Command | None) -> str:
        quote, anime, char = fetch(
            f"{self.URL}",
            ["data.content", "data.anime.name", "data.character.name"],
        )
        return f"{quote} -{char}({anime})"

    def ping(self) -> bool:
        return bool(self.run(None))
