from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Meme(BaseAPI):
    """TODO"""

    URL = "https://meme-api.com/gimme"

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "meme"

    def run(self, cmd: Command | None) -> str:
        nsfw = True
        while nsfw:
            url, nsfw = fetch(self.URL, ["url", "nsfw"])
        return url

    def ping(self) -> bool:
        return bool(self.run(None))
