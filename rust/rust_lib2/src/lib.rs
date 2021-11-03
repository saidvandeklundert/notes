extern crate libc;
extern crate serde;
extern crate serde_json;

use libc::c_char;
use serde::{Deserialize, Serialize};
use serde_json::json;
use std::ffi::CStr;
use std::ffi::CString;
use std::str;

#[derive(Debug, Serialize, Deserialize)]
struct PythonModel {
    timeout: u8,
    retries: u8,
    host_list: Vec<String>,
    action: String,
}

#[derive(Serialize, Deserialize)]
struct RustResult {
    result: String,
    message: String,
    failed_hosts: Vec<String>,
}

#[no_mangle]
pub extern "C" fn start_procedure(c_string_ptr: *const c_char) -> *mut c_char {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let string = str::from_utf8(bytes).unwrap();
    let model: PythonModel = serde_json::from_str(string).unwrap();
    println!("Taking action using following input:\n{:?}", model);
    let result = RustResult {
        result: "success".to_string(),
        message: "1 host failed".to_string(),
        failed_hosts: vec!["server1".to_string()],
    };
    let result_json = serde_json::to_string(&result).unwrap();
    let c_string = CString::new(result_json).unwrap();
    c_string.into_raw()
}
