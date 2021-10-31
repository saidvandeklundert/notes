extern crate libc;

use libc::c_char;
use std::ffi::CStr;
use std::ffi::CString;
use std::str;

/// Receive data from the Python universe and use it in Rust.
#[no_mangle]
pub extern "C" fn python_to_rust(value: *const c_char) -> *mut c_char {
    let c_value = unsafe { CStr::from_ptr(value).to_bytes() };
    let python_string = str::from_utf8(c_value);
    println!("Python string: {}", python_string.unwrap());
    let s = CString::new("Hello from Rust!").unwrap().into_raw();
    return s;
}
