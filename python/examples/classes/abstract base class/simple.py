from abc import ABC, abstractmethod
from dataclasses import dataclass


class Greeter(ABC):
    @abstractmethod
    def good_day(self) -> str:
        pass


@dataclass
class Human(Greeter):
    name: str
    age: int

    def good_day(self):
        return f"Hello, I am {self.name}"


jan = Human(name="jan", age=6)
print(jan.good_day())
