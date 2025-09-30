from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch, is_similar


class Riddle(BaseAPI):
    """Riddle: Two words, my answer is only two words. To keep me, you must give me.
    Answer: Your word
    riddle: Generates a riddle
    idk: Writes answer for last riddle"""

    def __init__(self) -> None:
        self.answer = ""

    def validate(self, cmd: Command) -> bool:
        return (
            is_similar(cmd.message, self.answer)
            or cmd.command == "riddle"
            or cmd.command == "idk"
        )

    def run(self, cmd: Command) -> str:
        if cmd.command == "riddle":
            return self.get_riddle()
        answer = self.answer
        self.answer = ""
        return answer

    def ping(self) -> bool:
        return bool(self.get_riddle())

    def get_riddle(self):
        url = "https://riddles-api.vercel.app/random"
        riddle, answer = fetch(url, ["riddle", "answer"])
        self.answer = answer.lower()
        return riddle
