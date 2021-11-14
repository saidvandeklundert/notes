extern crate serde;
extern crate serde_json;
use log::{debug, error, info, warn};
use pyo3::exceptions::PyOSError;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3_log;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

use std::fmt;

/// Multiply two numbers:
#[pyfunction]
fn multiply(a: isize, b: isize) -> PyResult<isize> {
    Ok(a * b)
}

/// Return the sum of a list/vector of numbers
#[pyfunction]
fn list_sum(a: Vec<isize>) -> PyResult<isize> {
    let mut sum: isize = 0;
    for i in a {
        sum += i;
    }
    Ok(sum)
}

/// Print every item of a list to console:
#[pyfunction]
fn list_printer(a: Vec<String>) {
    for string in a {
        println!("{}", string)
    }
}

// Print all the key values in a dict to console:
#[pyfunction]
fn dict_printer(hm: HashMap<String, String>) {
    for (key, value) in hm {
        println!("{} {}", key, value)
    }
}

/// Print every item in an array to console:
#[pyfunction]
fn array_printer(a: [String; 8]) {
    for string in a {
        println!("{}", string)
    }
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn human_says_hi(human_data: String) {
    println!("{}", human_data);
    let human: Human = serde_json::from_str(&human_data).unwrap();

    println!(
        "Now we can work with the struct:\n {:#?}.\n {} is {} years old.",
        human, human.name, human.age,
    )
}

#[derive(Debug, Serialize, Deserialize)]
struct Human {
    name: String,
    age: u8,
}

#[pyfunction]
fn log_different_levels() {
    error!("logging an error");
    warn!("logging a warning");
    info!("logging an info message");
    debug!("logging a debug message");
}

#[pyfunction]
fn log_example() {
    info!("A log message from {}!", "Rust");
}

#[pyfunction]
fn get_fibonacci(number: isize) -> PyResult<u128> {
    if number == 1 {
        return Ok(1);
    } else if number == 2 {
        return Ok(2);
    }

    let mut sum = 0;
    let mut last = 0;
    let mut curr = 1;
    for i in 1..number {
        sum = last + curr;
        last = curr;
        curr = sum;
    }
    Ok(sum)
}

// Raising an exception in a function called 'greater_than_2', which is defined later on:

// Define 'MyError' as a custom exception:
#[derive(Debug)]
struct MyError {
    /*
    the 'message' field that is used later on
    to be able print any message.
    */
    pub msg: &'static str,
}

// Implement the 'Error' trait for 'MyError':
impl std::error::Error for MyError {}

// Implement the 'Display' trait for 'MyError':
impl fmt::Display for MyError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Error from Rust: {}", self.msg)
    }
}

//
impl std::convert::From<MyError> for PyErr {
    fn from(err: MyError) -> PyErr {
        PyOSError::new_err(err.to_string())
    }
}

#[pyfunction]
fn greater_than_2(number: isize) -> Result<isize, MyError> {
    if number <= 2 {
        return Err(MyError {
            msg: "number is less than or equal to 2",
        });
    } else{
        return Ok(number);
    
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    pyo3_log::init();
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(multiply, m)?)?;
    m.add_function(wrap_pyfunction!(list_sum, m)?)?;
    m.add_function(wrap_pyfunction!(list_printer, m)?)?;
    m.add_function(wrap_pyfunction!(dict_printer, m)?)?;
    m.add_function(wrap_pyfunction!(array_printer, m)?)?;
    m.add_function(wrap_pyfunction!(human_says_hi, m)?)?;
    m.add_wrapped(wrap_pyfunction!(log_example))?;
    m.add_wrapped(wrap_pyfunction!(log_different_levels))?;
    m.add_function(wrap_pyfunction!(get_fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(greater_than_2, m)?)?;

    Ok(())
}
