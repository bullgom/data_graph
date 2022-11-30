from abc import ABC, abstractmethod

# I don't like this, but can't find a better way.
class Receiver(ABC):
    @abstractmethod
    def ready(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def generate(self) -> None:
        raise NotImplementedError
