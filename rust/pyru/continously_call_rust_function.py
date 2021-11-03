from pydantic import BaseModel
import ctypes


class Person(BaseModel):
    name: str
    age: int


library_name = "target/release/libpyru.so"

pyru = ctypes.CDLL(library_name)

if __name__ == "__main__":
    i = 0
    loops = 1000000000000000
    while i < loops:
        marie = Person(name="Marie", age=2)
        marie_json_str = marie.json(indent=2).encode("utf-8")
        rust_return_marie = pyru.python_to_rust(marie_json_str)
        rust_return_bytes = ctypes.c_char_p(rust_return_marie)
        rust_return_string = rust_return_bytes.value

        if rust_return_string:
            rust_return_string = rust_return_string.decode("utf-8")

        if i % 10000 == 0:
            print(f"Rust return: {rust_return_string}")
            percent_done = str(int(i / loops * 100))
            print(f"percent done: {percent_done}")
        # pyru.free_rust_mem(rust_return_marie)
        marie, rust_return, rust_return_bytes, rust_return_marie = (
            None,
            None,
            None,
            None,
        )

        i += 1
