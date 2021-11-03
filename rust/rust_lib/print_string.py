import ctypes

rust = ctypes.CDLL("target/release/librust_lib.so")


if __name__ == "__main__":
    SOME_BYTES = "Python says hi inside Rust!".encode("utf-8")
    rust.print_string(SOME_BYTES)

    rust.print_string(
        ctypes.c_char_p("Another way of sending strings to Rust via C.".encode("utf-8"))
    )
