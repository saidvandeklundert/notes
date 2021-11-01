import ctypes
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


pyru = ctypes.CDLL("target/release/libpyru.so")

if __name__ == "__main__":
    marie = Person(name="Marie", age=2)
    marie_json_string = marie.json(indent=2).encode("utf-8")

    rust_return = pyru.python_to_rust(marie_json_string)
    # Read the return from Rust as a string:
    rust_return_string = ctypes.c_char_p(rust_return).value
    if rust_return_string:
        rust_return_string = rust_return_string.decode("utf-8")
        print(f"Rust returned the following:\n{rust_return_string}")

    # free the memory allocated by Rust:
    pyru.free_rust_mem(rust_return)