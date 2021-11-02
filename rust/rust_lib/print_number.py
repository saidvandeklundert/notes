import ctypes

rust_lib = ctypes.CDLL("target/release/librust_lib.so")

if __name__ == "__main__":
    SOME_MORE_BYTES = (2).to_bytes(4, byteorder="little")
    rust_lib.print_int(SOME_MORE_BYTES)

    SOME_BYTES = (100).to_bytes(4, byteorder="little")
    rust_lib.print_int(SOME_BYTES)

    SOME_MORE_BYTES = (2147483648).to_bytes(4, byteorder="little")
    rust_lib.print_int(SOME_MORE_BYTES)
