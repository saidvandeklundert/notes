import ctypes
from sys import argv

rust = ctypes.CDLL("target/release/librust_lib.so")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./print_string_reversed.py <string>")
        exit(1)
    rust_return_ptr = rust.reverse_string("Hello, World!".encode("utf-8"))
    rust_return_bytes = ctypes.c_char_p(rust_return_ptr).value
    if rust_return_bytes:
        rust_return_string = rust_return_bytes.decode("utf-8")
        print(f"Rust returned the following:\n{rust_return_string}")

    rust.free_string(rust_return_ptr)