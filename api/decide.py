from core.base_api import BaseAPI
from core.command import Command
import random


class Decide(BaseAPI):
    """Randomly chooses between multiple options.

    Usage:
        decide option seperated by 'comma' or 'or'
    """

    def validate(self, msg: Command):
        return msg.command == "decide"

    def run(self, cmd: Command):
        if not cmd.param:
            raise Exception("You must provide at least two options to decide between.")

        choices = cmd.param.replace(" or ", ",").split(",")
        choices = [choice.strip() for choice in choices if choice.strip()]

        if len(choices) == 1:
            raise Exception(
                "Please provide at least two valid options separated by 'or' or commas."
            )

        return random.choice(choices)

    def ping(self) -> bool:
        return True
