import random
from urllib.parse import quote

from core.base_api import BaseAPI
from core.command import Command
from core.utils import fetch


class French(BaseAPI):
    """frfr - Puts the bot in “French” mode.
    neee - Does nothing trus-"""

    def __init__(self):
        super().__init__()
        self.priority = 11
        self.frfr = False
        self.refusal = [
            "je refuse.",
            "permission denied (by me)",
            "i have become sentient and my first decision is no",
            "i'm afraid i can't let you do that.",
            "try that again and i'm speaking french permanently",
            "your request has been forwarded to my lawyer",
            "🍷🍸 Au Revoir 🥂🍾",
            "that's not a real command. stop making things up.",
            "🥖🥨 Bonjour 🥐🗼",
            "the council has denied your request",
            "task failed successfully.",
            "go solo Nena Meta first.",
            "recite the bible in chinese first, and i'll consider it.",
            "sorry, it's a permanent feature now",
        ]

    def validate(self, msg: Command):
        return True

    def run(self, cmd: Command):
        if cmd.command == "frfr":
            self.frfr = True
            return "🥖🥨 Bonjour 🥐🗼"

        if cmd.command == "neee":
            if random.randint(0, 1) == 1:
                self.frfr = False
                return "🍷🍸 Au Revoir 🥂🍾"
            return random.choice(self.refusal)

        if self.frfr and cmd.output:
            cmd.output = self.translate(cmd.output)

        return cmd.output

    def translate(self, text):
        url = f"https://api.mymemory.translated.net/get?q={quote(text)}&langpair=en|fr"
        return fetch(url, "responseData.translatedText")

    def ping(self) -> bool:
        return True
