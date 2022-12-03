# python -m mypy .\07_callables.py
from typing import Callable


def add_one(x: int) -> int:
    """Used as callback later on"""
    return x + 1


def multiply_by_two(x: int) -> int:
    """Used as callback later on"""
    return x * 2


def multiply_to_numbers(a: int, b: int) -> int:
    return a * b


# Callable[[arg types], return type]
# Callable[[int], int]
def higher_order_function(f: Callable[[int], int], x: int) -> int:
    """Higher order function

    The caller that runs the callback function."""
    return f(x)


print(higher_order_function(add_one, 4))
print(higher_order_function(multiply_by_two, 4))
print(higher_order_function(multiply_to_numbers, 4))

# aliasing

Computation = Callable[[int], int]


def another_func(f: Computation, x: int) -> int:
    """Higher order function

    The caller that runs the callback function."""
    return f(x)


print(another_func(add_one, 4))
print(another_func(multiply_by_two, 4))
print(another_func(multiply_to_numbers, 4))


# any number of functions
Computation = Callable[..., int]
