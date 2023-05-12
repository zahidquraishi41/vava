import discord as dc

class Message:
    """
    Extracts essential information from a discord.Message object.
    """

    def __init__(self, message: dc.Message = None) -> None:
        """
        Constructs an instance of the Message class.

        Args:
            message : A discord.Message object to extract information from.

        Returns:
            None
        """
        if message:
            self.author = message.author.name
            self.is_admin = self.author == 'knemkaos'
            self.content = message.content.lower().strip()

    @property
    def is_command(self):
        """
        Checks if the message is meant for Vava.

        Returns:
            True if the message is meant for Vava, False otherwise.
        """
        return self.content == 'vava' or self.content.startswith('vava ')

    @property
    def command(self):
        """
        Returns the command portion of the message.

        Returns:
            The command portion of the message, or an empty string if the message is not a command.
        """
        if self.is_command and self.content.startswith('vava '):
            return self.content[5:]
        return ''

    def testInstance(content=None, author=None, is_admin=None):
        """
        Creates a Message instance for debugging purposes.

        Args:
            content : The content of the message.
            author : The name of the author of the message.
            is_admin : Indicates whether the author is an admin.

        Returns:
            An instance of the Message class with the specified attributes.
        """
        msg = Message()
        msg.author = author
        msg.is_admin = is_admin
        msg.content = content.lower().strip()
        return msg
