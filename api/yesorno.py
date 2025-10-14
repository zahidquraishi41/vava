from core.base_api import BaseAPI
from core.command import Command
import random
import re


class YesOrNo(BaseAPI):
    """Checks if the message is a yes/no question directed at Vava and returns a random yes/no style answer if true."""

    def __init__(self):
        super().__init__()
        self.priority = 6
        self.yes_no_patterns = (
            r"\bshould\b",
            r"\bshud\b",
            r"\bdo\b",
            r"\bis\b",
            r"\bare\b",
            r"\bcan\b",
            r"\bwill\b",
            r"\bwould\b",
            r"\bwud\b",
            r"\bcould\b",
            r"\bcud\b",
            r"\bwas\b",
            r"\bdid\b",
        )
        self.responses = (
            "Yes!",
            "No",
            "Absolutely",
            "No way",
            "Sure thing!",
            "I don’t think so",
            "Definitely!",
            "Not really",
            "Yup",
            "Nah",
        )

    def validate(self, cmd: Command):
        if not re.search(r"\bvava\b", cmd.message):
            return False
        return any(re.search(p, cmd.message) for p in self.yes_no_patterns)

    def run(self, cmd: Command):
        return random.choice(self.responses)

    def ping(self) -> bool:
        return True
