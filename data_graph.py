from typing import List
from .data_node import BaseDataNode


class DataGraph:
    def __init__(self) -> None:
        self.nodes: List[BaseDataNode] = []
    
    def add(self, node: BaseDataNode) -> None:
        self.nodes.append(node)
    
    def reset(self) -> None:
        for node in self.nodes:
            node.reset()
