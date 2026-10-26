from urllib.parse import quote

from core.base_api import BaseAPI
from core.command import Command
from uuid import uuid4



class Cat(BaseAPI):
    """Meow Eowm Owme Wmeo"""

    URL = "https://cataas.com/cat"

    def __init__(self) -> None:
        super().__init__()
        self.priority = 11

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "cat"

    def run(self, cmd: Command | None) -> str:
        text = None
        if cmd and cmd.param and " " in cmd.param:
            k, v = cmd.param.split(" ", 1)
            if k == "saying":
                text = v.strip() if v.strip() else None
        if text:
            return f"{self.URL}/says/{quote(text)}?cache={uuid4().hex}"

        return f"{self.URL}?cache={uuid4().hex}"

    def ping(self) -> bool:
        return bool(self.run(None))
