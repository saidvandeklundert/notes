extern crate libc;
extern crate serde;
extern crate serde_json;
use libc::c_char;
use serde::{Deserialize, Serialize};
use serde_json::json;
use std::ffi::CStr;
use std::ffi::CString;
use std::str;

/// Receive data from the Python universe and use it in Rust.
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

/// Ensure that a value is released from memory.
/// The value passed to this function is the 'CString::new' returned from a Rust function
///  called in the Python-verse.
#[no_mangle]
pub extern "C" fn free_rust_mem(c: *mut c_char) {
    // convert the pointer back to `CString`
    // it will be automatically dropped immediately
    //println!("Rust memory freed from Python!");
    unsafe {
        CString::from_raw(c);
    }
}

// Extra func working with the datamodel as a struct

#[derive(Debug, Deserialize, Serialize)]
struct Person {
    name: String,
    age: usize,
}

#[no_mangle]
pub extern "C" fn person_in_rust_says_hello(c_string_ptr: *const c_char) {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let string_from_python = str::from_utf8(bytes).unwrap();
    let person: Person = serde_json::from_str(&string_from_python).unwrap();
    println!("{} says hello in Rust", person.name);
}

#[no_mangle]
pub extern "C" fn rust_says_hello() {
    println!("Hello from the Rust universe!");
}
