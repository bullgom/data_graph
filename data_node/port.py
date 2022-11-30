from .base_class import BaseClass
from typing import Any


class Port(BaseClass):
    """Holds the generated data"""

    def __init__(self) -> None:
        super().__init__()
        self.reset()

    @property
    def data(self) -> Any:
        return self._data

    def put(self, data: Any) -> None:
        self._data = data

    def reset(self) -> None:
        self._data: Any | None = None
