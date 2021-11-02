import ctypes

rust = ctypes.CDLL("target/release/librust_lib.so")

if __name__ == "__main__":
    print(rust.reverse_string("Hello, World!"))
    rust.free_string()