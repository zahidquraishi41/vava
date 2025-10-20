from core.base_api import BaseAPI
from core.command import Command
import random
import re


class YesOrNo(BaseAPI):
    """
    Detects yes/no questions directed at Vava and returns a random yes/no style answer.
    Uses context-aware verb+subject patterns to avoid false positives.
    """

    def __init__(self):
        super().__init__()
        self.priority = 6

        # Yes/no patterns (only valid question structures)
        self.yes_no_patterns = (
            r"\bshall\b",
            r"\bhave\b",
            r"\bmay\b",
            r"\bdid\b",
            r"\bwill\b",
            r"\bshould\b",
            r"\bwould\b",
            r"\bmust\b",
            r"\bwas\b",
            r"\bmight\b",
            r"\bare\b",
            r"\bdo\b",
            r"\bdoes\b"
            r"\bhas\b",
            r"\bcan\b",
            r"\bcould\b",
            r"\bis\b",
            r"\bam\b",
        )

        # Natural yes/no responses
        self.responses = (
            "Yes.",
            "No.",
            "Definitely.",
            "No way.",
            "I don’t think so.",
            "Yup.",
            "Nah.",
            "Probably.",
            "Maybe not.",
            "Most likely.",
            "Unlikely.",
        )

    def validate(self, cmd: Command):
        message = cmd.message.lower().strip()

        # Must mention Vava
        if not re.search(r"\bvava\b", message):
            return False

        # Ignore wh-questions
        if re.search(r"\b(who|what|when|where|why|how)\b", message):
            return False

        # Must match a yes/no pattern
        return any(re.search(p, message) for p in self.yes_no_patterns)

    def run(self, cmd: Command):
        return random.choice(self.responses)

    def ping(self) -> bool:
        return True
