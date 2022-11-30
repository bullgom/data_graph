from .base_class import BaseClass
from abc import abstractmethod
from typing import TypeVar, Generic, Callable

T = TypeVar("T")
GeneratingFunction = Callable[..., T]


class DataGenerator(BaseClass, Generic[T]):
    def __init__(self, generating_function: GeneratingFunction) -> None:
        self.generating_function = generating_function

    def generate(self, *args, **kwargs) -> T:
        """Generates the output data according to `generating_function`

        Returns:
            T: The generated output. Best if a single value (instead of tuple)
        """
        return self.generating_function(*args, **kwargs)

    def reset(self) -> None:
        # This class has no state
        return
