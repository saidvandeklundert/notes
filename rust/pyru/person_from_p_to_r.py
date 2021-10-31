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
pyru.python_person_to_rust(json_json_str)
