import ctypes
from pydantic import BaseModel

library_path = "target/release/libpyru.so"

pyru = ctypes.CDLL(library_path)


class Person(BaseModel):
    name: str
    age: int


if __name__ == "__main__":
    jan = Person(name="Jan", age=4)
    # output Person instance as JSON string, then convert it to bytes, encoded as utf-8:
    jan_json_str = jan.json(indent=2).encode("utf-8")
    pyru.person_in_rust_says_hello(jan_json_str)