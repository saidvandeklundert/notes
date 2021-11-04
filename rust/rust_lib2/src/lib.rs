extern crate serde;
extern crate serde_json;

use serde::{Deserialize, Serialize};
use std::ffi::CStr;
use std::ffi::CString;
use std::os::raw::c_char;
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
    let model: PythonModel = serde_json::from_str(string).unwrap();
    let result = long_running_task(model);
    let result_json = serde_json::to_string(&result).unwrap();
    let c_string = CString::new(result_json).unwrap();
    c_string.into_raw()
}

fn long_running_task(model: PythonModel) -> RustResult {
    let result = RustResult {
        result: "success".to_string(),
        message: "1 host failed".to_string(),
        failed_hosts: vec!["server1".to_string()],
        job_id: model.job_id,
    };
    return result;
}
