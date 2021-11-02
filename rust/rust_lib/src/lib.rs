extern crate libc;

use libc::c_char;
use libc::c_int;
use std::ffi::CStr;
use std::ffi::CString;
use std::str;

/// Turn a C-string into a string slice and print to console:
#[no_mangle]
pub extern "C" fn print_string(c_string_ptr: *const c_char) {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let str_slice = str::from_utf8(bytes).unwrap();
    println!("{}", str_slice);
}

// Turn a C-int into a &i32 and print to console:
#[no_mangle]
pub extern "C" fn print_int(c_int_ptr: *const c_int) {
    let int_ptr = unsafe { c_int_ptr.as_ref().unwrap() };
    println!("Python gave us number {}", int_ptr);
}
