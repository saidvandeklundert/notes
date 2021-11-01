extern crate libc;
extern crate serde;
extern crate serde_json;
use libc::c_char;
use serde::{Deserialize, Serialize};
use serde_json::json;
use std::ffi::CStr;
use std::ffi::CString;
use std::str;

/// Example function, called from a Python script here:
///  https://github.com/saidvandeklundert/python/blob/main/rust/pyru/call_rust_function_with_argument_and_return.py
///
#[no_mangle]
pub extern "C" fn python_to_rust(c_string_ptr: *const c_char) -> *mut c_char {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let python_string = str::from_utf8(bytes).unwrap();
    //println!("Python string: {}", python_string.unwrap());

    let s = CString::new(format!("Hello from Rust!\n{}", python_string))
        .unwrap()
        .into_raw();
    return s;
}

/// Ensure that a value is released from memory:
#[no_mangle]
pub extern "C" fn free_rust_mem(c: *mut c_char) {
    // convert the pointer back to `CString`, dropping it automatically.
    unsafe {
        CString::from_raw(c);
    }
}

// Extra func working with the datamodel as a struct
#[derive(Deserialize, Serialize)]
struct Person {
    name: String,
    age: usize,
}

/// Example function, called from a Python script here:
///  https://github.com/saidvandeklundert/python/blob/main/rust/pyru/call_rust_from_python_with_arg.py
#[no_mangle]
pub extern "C" fn person_in_rust_says_hello(c_string_ptr: *const c_char) {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let string_from_python = str::from_utf8(bytes).unwrap();
    let person: Person = serde_json::from_str(&string_from_python).unwrap();
    println!("{} says hello in Rust", person.name);
}

/// Example function, called from a Python script here:
///  https://github.com/saidvandeklundert/python/blob/main/rust/pyru/call_rust_from_python.py
#[no_mangle]
pub extern "C" fn rust_says_hello() {
    println!("Hello from the Rust universe!");
}
