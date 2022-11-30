from typing import List

from .base_class import BaseClass


class RequirementChecker(BaseClass):
    def __init__(self, requirements: List[str]) -> None:
        self.requirements = requirements
        self.reset()

    def generated(self, name: str) -> None:
        self.is_generated[name] = True

    def reset(self) -> None:
        self.is_generated = {name: False for name in self.requirements}

    def ready(self) -> bool:
        return all(self.is_generated.values())
