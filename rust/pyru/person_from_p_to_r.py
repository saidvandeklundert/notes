# In the python script, instantiate a 'Person' and send it to a Rust function as bytes
# On the Rust side, read the bytes as a string, load it as JSON and Deserialize it into a Person struct.
"""Part 1: setting up the Python person class:"""
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


jan = Person(name="Jan", age=6)

# output the model as JSON string, then convert to bytes encoded a utf-8:
json_json_str = jan.json(indent=2).encode("utf-8")

"""Part 2: Load the library that enables using the Rust functions in Python:"""
import ctypes

# following is where the Rust library should be located:
library_name = "target/release/libpyru.so"
# loading the library:
pyru = ctypes.CDLL(library_name)

# Using the library (send a string as bytes that are encoded as utf-8):
pyru.person_in_rust_says_hello(json_json_str)

if __name__ == "__main__":
    import sys

    # Make infinite function calls and monitor mem usage
    if len(sys.argv) > 1:
        while True:
            pyru.person_in_rust_says_hello(json_json_str)
