import ctypes

rust = ctypes.CDLL("target/release/librust_lib.so")


if __name__ == "__main__":
    some_bytes = "Python says hi!".encode("utf-8")
    rust.print_string(some_bytes)
