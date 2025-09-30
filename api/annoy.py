from core.base_api import BaseAPI
from core.command import Command


class Annoy(BaseAPI):
    """Someone is online but not paying attention? I got u covered.
    annoy [name] [count]: Mentions [name], [count] number of times. default count is 5."""

    def validate(self, cmd: Command) -> bool:
        return cmd.command in ("spam", "annoy", "mention")

    def run(self, cmd: Command) -> str:
        if len(cmd.mentions) == 0:
            raise Exception(
                "No mention found in the message.\nUsage: annoy @user <count>"
            )

        count = cmd.param.split()[-1]
        count = int(count) if count.isdigit() else 5
        if count > 30:
            raise Exception("Mention count exceeds the top limit.")

        user = cmd.mentions[0].mention
        return " ".join([user] * count)
