import rust
from pydantic import BaseModel

a_list = ["one", "two", "three"]
rust.list_printer(a_list)

another_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
rust.array_printer(another_list)
a_dict = {
    "key 1": "value 1",
    "key 2": "value 2",
    "key 3": "value 3",
    "key 4": "value 4",
}

try:
    rust.dict_printer("wrong type")
except TypeError as e:
    print(f"Caught a type error: {e}")

rust.dict_printer(a_dict)


class Human(BaseModel):
    name: str
    age: int


jan = Human(name="Jan", age=6)
rust.human_says_hi(jan.json())

# logging example:
import logging

FORMAT = "%(levelname)s %(name)s %(asctime)-15s %(filename)s:%(lineno)d %(message)s"
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.DEBUG)
logging.info("Logging from the Python code")
rust.log_example()
rust.log_different_levels()

# data class
from dataclasses import dataclass


@dataclass
class Person:
    """Make a person."""

    name: str
    age: int


marie = Person(name="Marie", age=2)


# fibonacci


def get_fibonacci(n):
    """Get the nth fibonacci number."""
    fib_seq = [0]
    while n > 0:
        n -= 1
        if len(fib_seq) == 1:
            fib_seq.append(1)
        else:
            last = fib_seq[-1]
            second_to_last = fib_seq[-2]
            fib_seq.append(last + second_to_last)

    return fib_seq[-1]


print(f"Fibonacci number in Python and in Rust:")
for i in range(10):
    res_python = get_fibonacci(i)
    res_rust = rust.get_fibonacci(i)
    print(f"\t{i}\t{res_python}\t{res_rust}")


print(get_fibonacci(150))
print(rust.get_fibonacci(150))