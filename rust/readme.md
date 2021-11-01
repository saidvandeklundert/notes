I love Python and I love Rust.

Python + Rust, omg!

Steps to using Rust inside Python:

1. create a new Cargo library project:
2. modify the Cargo.toml and specify we are building a shared library, example [here](https://github.com/saidvandeklundert/python/blob/main/rust/pyru/Cargo.toml)
3. write a FFI in Rust that is compatible with C
4. build the library using the regular `cargo build --release`
5. Create a Python program that loads the library and calls the function. On Linux, load the `.so` file.

An example library made by me is [pyru](https://github.com/saidvandeklundert/python/tree/main/rust/pyru).

## Note on Creating the FFI:

The `extern` keywork facilitates the creation of an FFI (Foreign Function Interface). It can be used to call functions in other languages or to create an interface that allows other languages to call Rust functions.

From the book of Rust:
```
We also need to add a #[no_mangle] annotation to tell the Rust compiler not to mangle the name of this function. Mangling is when a compiler changes the name we’ve given a function to a different name that contains more information for other parts of the compilation process to consume but is less human readable. Every programming language compiler mangles names slightly differently, so for a Rust function to be nameable by other languages, we must disable the Rust compiler’s name mangling.
```

Example function that can be called from C:

```rust
#[no_mangle]
pub extern "C" fn call_from_c() {
    println!("Just called a Rust function from C!");
}
```

## Loading the library in Python

A Rust function exported to C can be loaded into Python using the `CDLL` class located in `ctypes`. From the `CDLL` docstring:

```
An instance of this class represents a loaded dll/shared
 library, exporting functions using the standard C calling
 convention (named 'cdecl' on Windows).

The exported functions can be accessed as attributes, or by
 indexing with the function name.
```

The following is an example where `CDLL` us used to load the functions from `target/release/libpyru.so`. After loading the file, the `call_rust_from_python` function is called:

```python
import ctypes
library_name = "target/release/libpyru.so"

pyru = ctypes.CDLL(library_name)
pyru.call_rust_from_python()
```


The previous example function did not take any arguments. Sending arguments into Rust can be a bit tricky. In Python, you need to translate all the types used as arguments to the function to their counterpart in C. Then, in Rust, you need to translate the C-types into valid Rust types.

When you are returning something from a Rust function to the Python runtime, you have to go about it the other way around: Rust -> C - > Python.

In my opinion, a nice way to do this is by using a data class on the Python side and a struct on the Rust side.

From Python to Rust:
- output the dataclass as a JSON string
- convert the JSON string to bytes
- send the bytes over to the Rust function

Then, in Rust:
- build a C-string from the values passed in from Python (via C) by reading the bytes
- after reading the bytes, use `str::from_utf8` to turn it into a string
- then, deserialize the JSON-string into a struct that you can work with

In case you want the Rust function to return a value to Python, do the opposite. Serialize a struct to JSON, output it as a string and send the C-string into Python. Then, inside the Python runtime, read the C-string using `c_char_p` and transform it into a dataclass again.

## Calling a Rust function from Python:

```python
import ctypes

# pointer to the file containing the rust function:
library_path = "target/release/libpyru.so"

# the above file is relative to where this file is located.

# loading the library:
pyru = ctypes.CDLL(library_path)

if __name__ == "__main__":
    # calling the Rust function:
    pyru.rust_says_hello()
```

The Rust function that is called here is the following:

```rust
#[no_mangle]
pub extern "C" fn rust_says_hello() {
    println!("Hello from the Rust universe!");
}
```

## Calling a Rust function from Python with an argument:

```python
import ctypes
from pydantic import BaseModel

library_path = "target/release/libpyru.so"

pyru = ctypes.CDLL(library_path)


class Person(BaseModel):
    name: str
    age: int


if __name__ == "__main__":
    jan = Person(name="Jan", age=4)
    # output Person instance as JSON string, then convert it to bytes, encoded as utf-8:
    jan_json_str = jan.json(indent=2).encode("utf-8")
    pyru.person_in_rust_says_hello(jan_json_str)
```

On the Rust side, we have the following code:

```rust
#[no_mangle]
pub extern "C" fn person_in_rust_says_hello(c_string_ptr: *const c_char) {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let string_from_python = str::from_utf8(bytes).unwrap();
    let person: Person = serde_json::from_str(&string_from_python).unwrap();
    println!("{} says hello in Rust", person.name);
}


#[derive(Debug, Deserialize, Serialize)]
struct Person {
    name: String,
    age: usize,
}

```

In the function signature for `person_in_rust_says_hello`, we recieve the bytes as a `*const c_char`. This is a raw pointer to a C char value. Dereferencing a raw pointer must be done in an unsafe block, so on the next line, enter an unsafe block using `unsafe { ..}`. Inside the unsafe block, we pass the raw pointer to `CStr::from_ptr`. This function `will wrap the provided 'ptr' with a 'CStr' wrapper, which allows inspection and interoperation of non-owned C strings.` It returns a `CStr` on which we then call `.to_bytes()`, which will essentially convert the C string to a byte slice. Once the expression is run, the `bytes` variable will contain a `&[u8]` value. 

The `bytes` variable is fed to `str::from_utf8`, and after that happened, `string_from_python` contains the string we send from Python as an `&str`. We then proceed to use `serde_json::from_str` to marshal the string into a struct.

## Calling a Rust function that takes an argument and returns a value from Python:

In this case, we will call 2 Rust functions:
### python_to_rust: 

This Rust function will take and argument and return a value. The returned value is read in Python using `c_char_p`.

### free_rust_mem:

If we continously make function calls to Rust, the data that Rust returns into Python will not be dropped or garbage collected. To this end, we call the `free_rust_mem` function and pass it the value that the `python_to_rust` function returned to Python. Rust can then free that memory.

```python
import ctypes
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


pyru = ctypes.CDLL("target/release/libpyru.so")

if __name__ == "__main__":
    marie = Person(name="Marie", age=2)
    marie_json_string = marie.json(indent=2).encode("utf-8")

    rust_return = pyru.python_to_rust(marie_json_string)
    # Read the return from Rust as a string:
    rust_return_string = ctypes.c_char_p(rust_return).value
    if rust_return_string:
        rust_return_string = rust_return_string.decode("utf-8")
        print(f"Rust returned the following:\n{rust_return_string}")

    # free the memory allocated by Rust:
    pyru.free_rust_mem(rust_return)
```


```rust
/// Receive data from the Python universe and use it in Rust.
#[no_mangle]
pub extern "C" fn python_to_rust(value: *const c_char) -> *mut c_char {
    let c_value = unsafe { CStr::from_ptr(value).to_bytes() };
    let python_string = str::from_utf8(c_value).unwrap();

    let s = CString::new(format!("Hello from Rust!\n{}", python_string))
        .unwrap()
        .into_raw();
    return s;
}

#[derive(Debug, Deserialize, Serialize)]
struct Person {
    name: String,
    age: usize,
}

#[no_mangle]
pub extern "C" fn free_rust_mem(c: *mut c_char) {
    // convert the pointer back to `CString`
    // it will be automatically dropped immediately
    //println!("Rust memory freed from Python!");
    unsafe {
        CString::from_raw(c);
    }
}
```

## Summary

Sending bytes from the Python runtime to Rust makes it easy to reason about the data exchange between the two. Using JSON on both sides, we can marshal the bytes into a struct or a data class and treat the struct/data class as output and input between the two 'worlds'.


Rust does not have a GC, so we need to release memory on the Rust side in case we let Rust return a value. 

Using this pattern, reasoning about the calls from Python into Rust is not too difficult in my opinion.