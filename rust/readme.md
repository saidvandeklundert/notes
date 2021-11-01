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


The previous example function did not take any arguments. Sending arguments into Rust can be a bittricky. In Python, you need to translate all the types used as arguments to the function to their counterpart in C. Then, in Rust, you need to translate the C-types into valid Rust types.

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

## Python example, calling the Rust python_person_to_rust function:

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

jan = Person(name="Jan", age=6)
json_json_str = jan.json(indent=2).encode("utf-8")
pyru.python_person_to_rust(json_json_str)
```
## Example Rust function, that was previously called from Python:

In Rust, you can receive this as a `*const c_char`: 

```rust
#[no_mangle]
pub extern "C" fn python_person_to_rust(value: *const c_char) {
    let c_value = unsafe { CStr::from_ptr(value).to_bytes() };
    let python_string = str::from_utf8(c_value).unwrap();
    let person: Person = serde_json::from_str(&python_string).unwrap();
    println!("{} says hello in Rust", person.name);
}

#[derive(Debug, Deserialize, Serialize)]
struct Person {
    name: String,
    age: usize,
}

```

In the function signature, we recieve the bytes as a `*const c_char`. Using `CStr::from_ptr`, we take the pointer to the C string, and read the bytes. After that, we use `str::from_utf8` to read the bytes as utf8 and then.

After that, we use serde to read the JSON string into Person.

If we want to return something from Rust to Python, we could do something like this:
```rust
#[no_mangle]
pub extern "C" fn rust_function(value: *const c_char) -> *mut c_char {
    let c_value = unsafe { CStr::from_ptr(value).to_bytes() };
    let string = str::from_utf8(c_value).unwrap();    

    let s = CString::new(format!("Hello from Rust!\n{}", string))
        .unwrap()
        .into_raw();
    return s;
}
```

In the above function, we receive and read bytes into a variable called `string`. Then, we use `CString::new` to create a C compatible string. After that, `into_raw` is used to transfer ownership to C.


In Python, we can use `ctypes.c_char_p()` to read this return:

```python
import ctypes
library_name = "target/release/libpyru.so"
pyru = ctypes.CDLL(library_name)

rust_return = pyru.rust_function(argument)

rust_return_bytes = ctypes.c_char_p(rust_return)
string = rust_return_bytes.value
```

Sending bytes from the Python runtime to Rust makes it easy to reason about the data exchange between the two. Using JSON on both sides, we can marshal the bytes into a struct or a data class and treat the struct/data class as output and input between the two worlds.


Rust does not have a GC, so we need to release memory on the Rust side in case we let Rust return a value. This could look something like so:

```rust
#[no_mangle]
pub extern "C" fn free_rust_mem_from_python(c: *mut c_char) {
    // convert the pointer back to `CString`
    // it will be automatically dropped immediately
    //println!("Rust memory freed from Python!");
    unsafe {
        CString::from_raw(c);
    }
}
```

We call the function on the Python side after we are done with the Rust return. It could look something like so:

```python
import ctypes
from pydantic import BaseModel

library_name = "target/release/libpyru.so"
pyru = ctypes.CDLL(library_name)
rust_return = pyru.python_to_rust(json_json_str)

class Person(BaseModel):
    name: str
    age: int
marie = Person(name="Marie", age=2)
marie_json_str = marie.json(indent=2).encode("utf-8")

rust_return_marie = pyru.python_to_rust(marie_json_str)
rust_return_bytes = ctypes.c_char_p(rust_return_marie)
rust_return_string = rust_return_bytes.value

pyru.free_rust_mem_from_python(rust_return_marie)
```

Using this pattern, reasoning about the calls from Python into Rust is not too difficult in my opinion.