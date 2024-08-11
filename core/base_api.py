from core.command import Command
from abc import ABC, abstractmethod


class BaseAPI(ABC):
    priority = 5

    @abstractmethod
    def validate(self, cmd: Command) -> bool:
        pass

    @abstractmethod
    def run(self, cmd: Command) -> str:
        pass

    def ping(self) -> bool:
        return True
