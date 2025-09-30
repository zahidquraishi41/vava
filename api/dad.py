from core.base_api import BaseAPI
from core.command import Command


class Dad(BaseAPI):
    """Detects messages where the user mentions 'I'm' or 'I am' and responds with a humorous 'dad joke'
    You: I'm good
    Vava: Hello good, I'm vava."""

    def __init__(self) -> None:
        super().__init__()
        self.priority = 6

    def validate(self, cmd: Command) -> bool:
        return "i'm " in cmd.message or "i am " in cmd.message or "im" in cmd.message

    def run(self, cmd: Command) -> str:
        if "i'm " in cmd.message:
            user = cmd.message.split("i'm ", 1)[1]
        else:
            user = cmd.message.split("i am ", 1)[1]

        return f"Hello {user}, I am vava"
