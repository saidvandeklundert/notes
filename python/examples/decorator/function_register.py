from typing import Callable

FUNCTION_REGISTER = {}


def register_function(function: Callable):
    """Place the class for the event into the registry to make it     accessible in the module."""
    FUNCTION_REGISTER[function.__qualname__] = function
    return function


@register_function
def sum(a: int, b: int) -> int:
    return a + b


@register_function
def multiply(a: int, b: int) -> int:
    return a * b


def main():
    print(FUNCTION_REGISTER)
    for func in FUNCTION_REGISTER.values():
        print(func(4, 2))


if __name__ == "__main__":
    main()
