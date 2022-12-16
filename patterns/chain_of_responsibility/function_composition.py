from functools import reduce
from typing import Callable


ComposableFunction = Callable[[int], int]


def compose(*functions: ComposableFunction) -> ComposableFunction:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def add(x: int) -> int:
    return x + 2


def multiply(
    x: int,
) -> int:
    return x * 2


def main() -> None:
    number = add(multiply(add(4)))
    print(number)
    myfunc = compose(add, multiply, add)
    result = myfunc(4)
    print(result)


if __name__ == "__main__":
    main()
