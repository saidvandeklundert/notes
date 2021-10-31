import ctypes

# following is where the Rust library should be located:
library_name = "target/release/libpyru.so.so"
# loaing the library:
rust_code = ctypes.CDLL(library_name)
# Using the library:
print(rust_code.python_to_rust(b"banana", b"na"))
