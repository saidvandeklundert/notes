import ctypes

# following is where the Rust library should be located:
library_name = "target/release/libstringtools.so"
# loaing the library:
stringtools = ctypes.CDLL(library_name)
# Using the library:
print(stringtools.count_substrings(b"banana", b"na"))


while True:
    print(stringtools.count_substrings(b"banana", b"na"))