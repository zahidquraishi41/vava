from core.base_api import BaseAPI
from core.command import Command
import re


class Dad(BaseAPI):
    """Detects messages where the user mentions 'I'm' or 'I am' and responds with a humorous 'dad joke'
    You: I'm good
    Vava: Hello good, I'm vava."""

    def __init__(self) -> None:
        super().__init__()
        self.priority = 6
        self.pattern = re.compile(r"\b(?:i am|i['’]?m)\b\s+(.*)", re.IGNORECASE)

    def validate(self, cmd: Command) -> bool:
        return self.pattern.search(cmd.message)

    def run(self, cmd: Command) -> str:
        match = self.pattern.search(cmd.message)
        if match and match.group(1).strip():
            return f"Hello {match.group(1).strip()}, I am vava"
