from typing import Any

from .base_class import BaseClass
from .port import Port


class RequirementChecker(BaseClass):
    def __init__(self) -> None:
        self.requirements = []
        self.reset()

    def ready(self) -> bool:
        return all([port.data is not None for port in self.requirements])

    def requires(self, port: Port) -> None:
        self.requirements.append(port)

    def reset(self) -> None:
        return

    def gather_data(self) -> Any:
        return [port.data for port in self.requirements]
