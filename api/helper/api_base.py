import discord as dc


class APIBase:
    """
    An interface for all api.
    """

    def validate(self, msg: dc.Message):
        """
        Check if the message matches the command.

        Args:
            msg: A Command object representing the message sent by the user.

        Returns:
            True if the message matches the command, False otherwise.
        """
        raise NotImplementedError

    def run(self, msg: dc.Message):
        """
        Execute the command. Only invoked if validate() returns True.

        Args:
            msg: A Message object representing the message sent by the user.

        Returns:
            A string containing the bot's response to the command, or None if there is no response.
        """
        raise NotImplementedError

    def help(self):
        """
        Get help text for the command.

        Returns:
            A string containing help text for the command.
        """
        raise NotImplementedError
