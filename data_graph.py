from typing import Any, Callable, List, NoReturn, Tuple, TypeVar

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
        f: Callable[..., T] | None = None,
        *requirements: BaseDataNode,
    ) -> BaseDataNode:
        if (f is None) and (not requirements):
            node = RootDataNode(name)
        elif (f is not None) and (requirements):
            node = DataNode(name, f, *requirements)
        else:
            raise TypeError("Not possible combination")
        self.add_node(node)
        return node

    def reset(self) -> None:
        for node in self.nodes:
            node.reset()

    def find(self, name: str) -> BaseDataNode | NoReturn:
        for node in self.nodes:
            if node.name == name:
                return node

        raise ValueError(f"{name} doesn't exist")

    def datas_of(self, *names: str) -> Tuple[Any]:
        return tuple(map(self.data_of, names))

    def data_of(self, name: str) -> Any:
        return self.find(name).port.data

    def __getitem__(self, name: str) -> BaseDataNode:
        return self.find(name)

    def put(self, name: str, value: Any) -> None:
        self.find(name).put(value)
