from abc import ABC, abstractmethod
from dataclasses import dataclass


class Greeter(ABC):
    @abstractmethod
    def good_day(self) -> str:
        """Property to set the BR WF name which will be started
        User must implement this property in their subclass as their WF name is a variable
        """

    @abstractmethod
    def goodbye(self) -> str:
        """Property to set the BR WF name which will be started
        User must implement this property in their subclass as their WF name is a variable
        """


@dataclass
class Human(Greeter):
    name: str
    age: int

    def good_day(self):
        return f"Hello, I am {self.name}"


@dataclass
class FaultyHuman(Greeter):
    name: str
    age: int

    def good_day(self):
        return f"Hello, I am {self.name}"


jan = Human(name="jan", age=6)
print(jan.good_day())


hugo = FaultyHuman(name="Hugo", age=30)


def human_reporter(human: Human):
    print(human.good_day())
