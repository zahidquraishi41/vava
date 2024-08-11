import discord as dc
import os


class Command:
    def __init__(self, message: dc.Message) -> None:
        self.author = message.author.name
        self.mentions = message.mentions
        self.output = None
        self.is_admin = os.environ['ADMIN_USERNAME'] == self.author

        self.message = message.content.lower().strip()
        tokens = self.message.split(maxsplit=2)
        while len(tokens) < 3:
            tokens.append('')
        self.is_command = tokens[0] == 'vava'
        self.command = tokens[1] if self.is_command else ''
        self.param = tokens[2] if self.is_command else ''
