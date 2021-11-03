use std::ffi::CStr;
use std::ffi::CString;
use std::os::raw::c_char;
use std::os::raw::c_int;
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

/// Turn a C-string into a slice, reverse it and return it as a C-string:
#[no_mangle]
pub extern "C" fn reverse_string(c_string_ptr: *const c_char) -> *mut c_char {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let str_slice = str::from_utf8(bytes).unwrap();
    let reversed_str = str_slice.chars().rev().collect::<String>();
    CString::new(reversed_str).unwrap().into_raw()
}

/// Free memory:
#[no_mangle]
pub extern "C" fn free_string(c_string_ptr: *mut c_char) {
    unsafe { CString::from_raw(c_string_ptr) };
}
