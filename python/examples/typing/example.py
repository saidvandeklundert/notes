"""
From current dir:
mypy.exe .\example.py
"""
from typing import Callable


def add_int(x: int) -> int:
    """Used as callback later on"""
    return x + 1


print(add_int(1))

# Callable[[int], int]
# funcname[[arg types], return type]
def higher_order_func(f: Callable[[int], int], x: int) -> int:
    """Higher order function

    The caller that runs the callback function."""
    return f(x)


print(higher_order_func(add_int, 1))


class Branata:
    def __init__(self, yolo: str):
        self.oloy = yolo


# 'cheating' with object
def user_of_branata(x: str) -> object:
    b = Branata(x)
    return b