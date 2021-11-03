extern crate libc;
extern crate serde;
extern crate serde_json;

use libc::c_char;
use serde::{Deserialize, Serialize};
use std::ffi::CStr;
use std::ffi::CString;
use std::str;

#[derive(Debug, Serialize, Deserialize)]
struct PythonModel {
    timeout: u8,
    retries: u8,
    host_list: Vec<String>,
    action: String,
    job_id: i32,
}

#[derive(Serialize, Deserialize)]
struct RustResult {
    result: String,
    message: String,
    failed_hosts: Vec<String>,
    job_id: i32,
}

#[no_mangle]
pub extern "C" fn start_procedure(c_string_ptr: *const c_char) -> *mut c_char {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let string = str::from_utf8(bytes).unwrap();
    //let model: PythonModel = serde_json::from_str(string).unwrap();
    let model: PythonModel = PythonModel {
        timeout: 10,
        retries: 3,
        host_list: vec!["s1".to_string(), "s2".to_string()],
        action: "action".to_string(),
        job_id: 1,
    };
    let result = long_running_task(model);
    let result_json = serde_json::to_string(&result).unwrap();
    let c_string = CString::new(result_json).unwrap();
    c_string.into_raw()
}

#[no_mangle]
pub extern "C" fn free_string(c_string_ptr: *mut c_char) {
    unsafe {
        CString::from_raw(c_string_ptr);
    }
}

fn long_running_task(model: PythonModel) -> RustResult {
    println!(
        "Starting long_running_task in Rust using following arguments:\n{:?} {:?} {:?}",
        model.retries, model.timeout, model.action
    );
    //println!("No GIL here. Lot's of possibilities to speed up Python.");
    //println!("Make sure to release the memory though!");
    let result = RustResult {
        result: "success".to_string(),
        message: "1 host failed".to_string(),
        failed_hosts: vec!["server1".to_string()],
        job_id: model.job_id,
    };
    return result;
}
