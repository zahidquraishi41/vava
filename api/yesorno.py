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
            # Personal/self
            r"\bam i\b",
            r"\bdo i\b",
            r"\bdid i\b",
            r"\bhave i\b",
            r"\bwas i\b",
            r"\bwill i\b",
            r"\bshould i\b",
            r"\bcould i\b",
            r"\bcan i\b",
            r"\bwould i\b",
            # General yes/no with pronouns
            r"\bhas he\b",
            r"\bhas she\b",
            r"\bhave we\b",
            r"\bhave you\b",
            r"\bhave they\b",
            r"\bis it\b",
            r"\bare we\b",
            r"\bare you\b",
            r"\bis there\b",
            r"\bwas it\b",
            # Modal + pronoun
            r"\bshould we\b",
            r"\bshould you\b",
            r"\bcan you\b",
            r"\bcould you\b",
            r"\bwill it\b",
            r"\bwould it\b",
            r"\bshall i\b",
            r"\bmay i\b",
            r"\bmight i\b",
            r"\bmust i\b",
            r"\bdo you\b",
            r"\bdid you\b",
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

        # Only trigger if it contains a question mark
        if "?" not in message:
            return False

        # Must match a yes/no pattern
        return any(re.search(p, message) for p in self.yes_no_patterns)

    def run(self, cmd: Command):
        return random.choice(self.responses)

    def ping(self) -> bool:
        return True
