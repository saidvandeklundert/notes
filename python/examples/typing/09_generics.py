# python -m mypy 09_generics.py
"""
For example, when you want to create a type that can take in 1
 other type, but you want to leave the decision as to what type
 that is to the user of the class.
"""
from typing import Generic, TypeVar

T = TypeVar("T")


class Barrel(Generic[T]):
    def __init__(self) -> None:
        self._store: dict[str, T] = {}

    def set_item(self, k: str, v: T) -> None:
        self._store[k] = v

    def get_item(self, k: str) -> T:
        return self._store[k]


if __name__ == "__main__":
    # create a barrel of int's:
    barrel_of_int = Barrel[int]()
    barrel_of_int.set_item("1", 1)
    barrel_of_int.set_item("2", 2)
    barrel_of_int.set_item("3", 3)
    barrel_of_int.get_item("3")
    # next will give a type error as we declared T to be of the type int.
    barrel_of_int.set_item("4", "4")

    # create a barrel of str's:
    barrel_of_int = Barrel[str]()
    barrel_of_int.set_item("1", "1")
    barrel_of_int.set_item("2", "2")
