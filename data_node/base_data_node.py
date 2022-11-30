from typing import Generic, List, TypeVar


from .receiver import Receiver
from .base_class import BaseClass
from .port import Port

T = TypeVar("T")


class BaseDataNode(BaseClass, Generic[T]):
    def __init__(self, name: str) -> None:
        self.name = name
        self.port = Port()

        self.receivers: List[Receiver] = []

    def register_node(self, other: Receiver) -> None:
        self.receivers.append(other)

    def reset(self) -> None:
        self.port.reset()

    def propagate(self) -> None:
        """Call the generation chain"""
        for receiver in self.receivers:
            if receiver.ready():
                receiver.generate()
