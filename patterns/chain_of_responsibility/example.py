from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional, Union


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """Default chaining behavior can be implemented inside a base
    handler class."""

    _next_handler: Union[Handler, None] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
Concrete handlers either handle a request or pass it to the next handler
in the chain.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I wil eath the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I will eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I will eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    Client code is usually suited to work with a single handler.

    Most oftentimes it is not even aware of the handler being part of a chain.
    """

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"    {result}")
        else:
            print(f"    {food} was left untouched.")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("chain: Monkey > Squirrel > Dog")
    client_code(monkey)

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
