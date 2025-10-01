from core.base_api import BaseAPI
from core.command import Command
import random
from gibberish import Gibberish


class Babble(BaseAPI):
    """Nuhonigu teget mefa derojow fomego bebedof

    Generates a random gibberish message. This command also acts as a fallback when an unknown command is entered.
    babble: Generates a random gibberish message.
    babble [length]: Generates a random gibberish message with the specified length."""

    def __init__(self):
        super().__init__()
        self.priority = 6

    def validate(self, cmd: Command) -> bool:
        return cmd.command == "babble" or (cmd.is_command and not cmd.output)

    def run(self, cmd: Command) -> str:
        if cmd.param and cmd.param.isdigit():
            sentence_length = int(cmd.param)
        else:
            sentence_length = random.randint(3, 7)

        return " ".join(Gibberish().generate_words(sentence_length))

    def ping(self) -> bool:
        return True
