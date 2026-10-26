from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Poem(BaseAPI):
    """TODO"""

    URL = "https://poetrydb.org/linecount,random/4-12;1"

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "poem"

    def run(self, cmd: Command | None) -> str:
        poem = fetch(f"{self.URL}", "0")
        title = poem["title"] + "  -" + poem["author"]
        lines = "\n".join(poem["lines"])
        return title + "\n\n" + lines

    def ping(self) -> bool:
        return bool(self.run(None))
