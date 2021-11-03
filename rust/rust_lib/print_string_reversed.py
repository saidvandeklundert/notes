import ctypes

rust = ctypes.CDLL("target/release/librust_lib.so")

if __name__ == "__main__":

    string_to_reverse = "Hello world. How are things?"

    rust_return_ptr = rust.reverse_string(string_to_reverse.encode("utf-8"))
    rust_return_bytes = ctypes.c_char_p(rust_return_ptr).value
    if rust_return_bytes:
        rust_return_string = rust_return_bytes.decode("utf-8")
        print(f"Rust returned the following:\n{rust_return_string}")

    rust.free_string(rust_return_ptr)