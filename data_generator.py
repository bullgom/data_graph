from .base_class import BaseClass
from abc import abstractmethod
from typing import TypeVar, Generic, Callable

T = TypeVar("T")


class DataGenerator(BaseClass, Generic[T]):
    def __init__(self, generating_function: Callable[..., T] | None = None) -> None:
        self.generating_function = generating_function

    def generate(self, *args, **kwargs) -> T:
        """Generates the output data according to `generating_function` if not None.
        If None, this function must be overriden

        Returns:
            T: The generated output. Best if a single value (instead of tuple)
        """
        if not self.generating_function:
            raise ValueError(f"Generating function hasn't been defined!")

        return self.generating_function(*args, **kwargs)

    def reset(self) -> None:
        # This class has no state
        return
