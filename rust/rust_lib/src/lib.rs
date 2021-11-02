extern crate libc;

use libc::c_char;
use std::ffi::CStr;
use std::ffi::CString;
use std::str;

/// Print a C string to console:
#[no_mangle]
pub extern "C" fn print_string(c_string_ptr: *const c_char) {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let str_slice = str::from_utf8(bytes).unwrap();
    println!("{}", str_slice);
}
