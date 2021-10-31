# script that calls a rust function from the pyru library.
# first part creates a pydantic basemodel class.
## second part loads the Rust function and sends over the pydantic model.
"""Part 1"""
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


jan = Person(name="Jan", age=6)

# output the model as JSON string, then convert to bytes encoded a utf-8:
json_json_str = jan.json(indent=2).encode("utf-8")
"""Part 2"""
import ctypes

# following is where the Rust library should be located:
library_name = "target/release/libpyru.so"
# loaing the library:
pyru = ctypes.CDLL(library_name)


# Using the library (send a string as bytes that are encoded as utf-8):
rust_return = pyru.python_to_rust(json_json_str)

# take the return value and convert it to a string:
import ctypes

rust_return_bytes = ctypes.c_char_p(rust_return)
rust_return_string = rust_return_bytes.value

if rust_return_string:
    rust_return_string = rust_return_string.decode("utf-8")

print(rust_return_string)
print(f"Rust return: {rust_return}")
# Using the library (send a string as bytes that are encoded as utf-8):
pyru.free_rust_mem_from_python(rust_return)

rust_return = None
i = 0
loops = 100000
while i < loops:
    marie = Person(name="Marie", age=2)
    marie_json_str = marie.json(indent=2).encode("utf-8")
    rust_return_marie = pyru.python_to_rust(marie_json_str)
    rust_return_bytes = ctypes.c_char_p(rust_return_marie)
    rust_return_string = rust_return_bytes.value

    if rust_return_string:
        rust_return_string = rust_return_string.decode("utf-8")

    if i % 1000 == 0:
        print(rust_return_string)
        print(f"Rust return: {rust_return}")
        percent_done = str(int(i / loops * 100))
        print(f"percent done: {percent_done}")
    pyru.free_rust_mem_from_python(rust_return_marie)
    marie = None
    rust_return = None
    rust_return_bytes = None
    rust_return_marie = None
    i += 1
