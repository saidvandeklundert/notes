import ctypes

# pointer to the file containing the rust function:
library_path = "target/release/libpyru.so"


# the above file is relative to where this file is located.

# loading the library:
pyru = ctypes.CDLL(library_path)

if __name__ == "__main__":
    # calling the Rust function:
    pyru.rust_says_hello()