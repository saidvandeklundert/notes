import ctypes

rust_lib = ctypes.CDLL("target/release/librust_lib.so")

if __name__ == "__main__":
    SOME_BYTES = (1231254687).to_bytes(4, byteorder="little")
    rust_lib.print_int(SOME_BYTES)