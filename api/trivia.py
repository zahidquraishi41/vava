from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class Trivia(BaseAPI):
    """TODO"""

    URL = "https://opentdb.com/api.php?amount=20"

    def __init__(self) -> None:
        super().__init__()
        self.cached: list[dict] = []
        self.answer = None

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "trivia" or cmd.command == "answer"

    def run(self, cmd: Command) -> str:
        if not self.cached:
            results = fetch(self.URL, "results")
            self.cached = results
        if cmd.command == "answer":
            answer = ":3"
            if self.answer:
                answer = self.answer
                self.answer = None
            return answer
        trivia = self.cached.pop()
        self.answer = trivia["correct_answer"]
        return trivia["question"]

    def ping(self) -> bool:
        return bool(self.run(None))
