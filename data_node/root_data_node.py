from typing import Any
from .base_data_node import BaseDataNode


class RootDataNode(BaseDataNode):
    def put(self, data: Any) -> None:
        self.port.put(data)
        self.propagate()
