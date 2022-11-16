"""
a) Both generate_id and weekday are not pure functions. Why not? 
    How would you write tests for these functions?

b) Rewrite both functions so that they are pure functions. 
 Observe what happens to the main function after making this change. 
 Are the functions now easier to test? Are they easier to use as well?
"""
import random
import string
from datetime import datetime


def generate_id(length: int) -> str:
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def weekday() -> str:
    today = datetime.today()
    return f"{today:%A}"


def main() -> None:
    print(f"Today is a {weekday()}")
    print(f"Your id = {generate_id(10)}")


if __name__ == "__main__":
    main()
