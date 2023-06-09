from api.helper.api_base import APIBase
from api.helper.message import Message


class APIManager:
    """
    Manages a list of APIs that can be executed based on the contents of a Message object.
    """

    def __init__(self) -> None:
        """
        Constructs an instance of the APIManager class.
        Initializes an empty list to store registered APIs.
        """
        self.api_list = []

    def register(self, api: APIBase) -> None:
        """
        Registers an API to the manager.

        Args:
            api : An instance of a class that inherits from the APIBase class.

        Returns:
            None
        """
        self.api_list.append(api)

    def execute(self, msg: Message) -> str:
        """
        Executes the appropriate API based on the contents of a Message object.

        Args:
            msg : An instance of the Message class that contains the message to be processed.

        Returns:
            The output generated by the executed API.
        """
        # sorting api based on priority
        self.api_list.sort(key=lambda x: x.priority)

        output = None
        for api in self.api_list:
            if api.validate(msg):
                output = api.run(msg)
                output = output if output else ''
                return output
