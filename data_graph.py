from typing import Any, Callable, List, TypeVar

from .data_node import BaseDataNode, DataNode, RootDataNode

T = TypeVar("T")


class DataGraph:
    def __init__(self) -> None:
        self.nodes: List[BaseDataNode] = []

    def add_node(self, node: BaseDataNode) -> BaseDataNode:
        self.nodes.append(node)
        return node

    def new(
        self,
        name: str,
        f: Callable[..., T] = None,
        *requirements: BaseDataNode,
    ) -> BaseDataNode:
        if (f is None) and (not requirements):
            node = RootDataNode(name)
        elif (f is not None) and (requirements):
            node = DataNode(name, f, requirements)
        else:
            raise TypeError("Not possible combination")
        self.add_node(node)
        return node

    def reset(self) -> None:
        for node in self.nodes:
            node.reset()

    def find(self, name: str) -> BaseDataNode | None:
        for node in self.nodes:
            if node.name == name:
                return node

        return None

    def get(self, name: str) -> Any:
        if (node := self.find(name)) is None:
            raise ValueError(f"{name} doesn't exist")

        return node.port.data

    def __getitem__(self, name: str) -> BaseDataNode:
        if (node := self.find(name)) is None:
            raise ValueError(f"{name} doesn't exist")

        return node
