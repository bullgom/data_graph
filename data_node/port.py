from .base_class import BaseClass
from typing import Generic, TypeVar

T = TypeVar("T")


class Port(BaseClass, Generic[T]):
    """Holds the generated data"""

    def __init__(self) -> None:
        super().__init__()
        self.reset()

    @property
    def data(self) -> T:
        return self._data

    def put(self, data: T) -> None:
        self._data = data

    def reset(self) -> None:
        self._data: T | None = None
