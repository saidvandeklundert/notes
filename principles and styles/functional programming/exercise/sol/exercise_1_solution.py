import random
import string
from datetime import datetime
from functools import partial
from typing import Callable

SelectionFn = Callable[[], str]


def generate_id(length: int, sel_fn: SelectionFn) -> str:
    return "".join(sel_fn() for _ in range(length))


def weekday(date: datetime) -> str:
    return f"{date:%A}"


def main() -> None:
    print(f"Today is a {weekday(datetime.today())}")
    sel_fn: SelectionFn = partial(
        random.choice, seq=string.ascii_uppercase + string.digits
    )  # type: ignore
    print(f"Your id = {generate_id(10, sel_fn)}")


if __name__ == "__main__":
    main()
