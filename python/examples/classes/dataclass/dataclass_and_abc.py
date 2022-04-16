from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Human(ABC):
    name: str
    age: int

    def __post_init__(self):
        self.post_initialization_enhancement()

    @abstractmethod
    def post_initialization_enhancement(self):
        pass


@dataclass
class Jan(Human):
    def post_initialization_enhancement(self):
        self.name = self.name.upper()


if __name__ == "__main__":
    jan = Jan(name="Jan", age=6)
    print(jan.name)
