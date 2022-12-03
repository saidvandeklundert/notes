use num_bigint::BigUint;
use num_traits::{One, Zero};
use pyo3::prelude::*;
use std::mem::replace;

#[pyfunction]
fn fib_in_rust_recursive(number: u128) -> PyResult<u128> {
    Ok(get_nth_fib(number))
}

fn get_nth_fib(number: u128) -> u128 {
    match number {
        1 => return number,
        2 => return number,
        _ => return get_nth_fib(number - 1) + get_nth_fib(number - 2),
    }
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

#[pyfunction]
fn get_fibonacci_big(number: isize) -> PyResult<String> {
    let mut f0: BigUint = Zero::zero();
    let mut f1: BigUint = One::one();
    for _ in 1..number {
        let f2 = f0 + &f1;
        // This is a low cost way of swapping f0 with f1 and f1 with f2.
        f0 = replace(&mut f1, f2);
    }
    let ret = format!("{}", f0);
    Ok(ret)
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib_in_rust_recursive, m)?)?;
    m.add_function(wrap_pyfunction!(get_fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(get_fibonacci_big, m)?)?;
    Ok(())
}
