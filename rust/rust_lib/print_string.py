import ctypes

rust = ctypes.CDLL("target/release/librust_lib.so")


if __name__ == "__main__":
    SOME_BYTES = "Python says hi inside Rust!".encode("utf-8")
    rust.print_string(SOME_BYTES)
