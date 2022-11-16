from typing import Callable


def create_multiplier(n: int) -> Callable:
    def multiplier(x: int):
        return x * n

    return multiplier


# alternative
from functools import partial


def multiplier(x: int, y: int) -> int:
    return x * y


triple = partial(multiplier, y=3)

if __name__ == "__main__":
    times_3 = create_multiplier(3)

    result = times_3(3)
    print(result)

    print(triple(3))
