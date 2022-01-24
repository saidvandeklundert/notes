from typing import Protocol
from dataclasses import dataclass


class Speaker(Protocol):
    def say_hi(self) -> str:
        ...


@dataclass
class Human:
    name: str
    age: int

    def say_hi(
        self,
    ) -> str:
        return "Hi, how are you?"


@dataclass
class Developer:
    name: str
    age: int

    def say_hi(
        self,
    ) -> str:
        return "Hi."


def greet(person: Speaker):
    greeting = person.say_hi()
    print(greeting)


if __name__ == "__main__":
    marie = Human(name="marie", age=3)
    said = Developer(name="said", age=36)
    greet(marie)
    greet(said)
