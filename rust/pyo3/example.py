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