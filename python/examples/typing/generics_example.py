"""
python -m mypy .
python -m mypy generics_example.py
"""
from typing import Dict, Generic, TypeVar

T = TypeVar("T")


class Registry(Generic[T]):
    def __init__(self) -> None:
        self._store: Dict[str, T] = {}

    def set_item(self, k: str, v: T) -> None:
        self._store[k] = v

    def get_item(self, k: str) -> T:
        return self._store[k]


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
