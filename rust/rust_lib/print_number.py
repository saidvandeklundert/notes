import ctypes

rust_lib = ctypes.CDLL("target/release/librust_lib.so")

if __name__ == "__main__":
    rust_lib.print_number(65234234)