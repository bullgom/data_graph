from abc import ABC, abstractmethod


class BaseClass(ABC):
    """A base class which all the classes of DataGraph library must inherit"""

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError
