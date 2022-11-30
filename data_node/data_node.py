from typing_extensions import Self

from .data_generator import DataGenerator, GeneratingFunction
from .requirement_checker import RequirementChecker
from .base_data_node import BaseDataNode
from .receiver import Receiver


class DataNode(BaseDataNode, Receiver):
    def __init__(self, name: str, generator_function: GeneratingFunction) -> None:
        super().__init__(name)
        self.checker = RequirementChecker()
        self.generator = DataGenerator(generator_function)

    def requires(self, data_node: Self) -> None:
        self.checker.requires(data_node.port)
        data_node.register_node(self)

    def generate(self) -> None:
        data = self.generator.generate(self.checker.gather_data())
        self.port.put(data)

        self.propagate()

    def ready(self) -> bool:
        return self.checker.ready()

    def reset(self) -> None:
        super().reset()
        self.checker.reset()
        self.generator()
