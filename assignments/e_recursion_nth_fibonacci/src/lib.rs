use num_bigint::BigUint;
use num_traits::{One, Zero};
use pyo3::prelude::*;

#[pyfunction]
fn fib_in_rust_recursive(number: u32) -> PyResult<u32> {
    Ok(get_nth_fib(number))
}

fn get_nth_fib(number: u32) -> u32 {
    match number {
        1 => return number,
        2 => return number,
        _ => return get_nth_fib(number - 1) + get_nth_fib(number - 2),
    }
}

#[pyfunction]
fn get_fibonacci(number: u128) -> PyResult<u128> {
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

fn get_fibonacci_big(number: u128) -> PyResult<BigUint> {
    if number == 1 {
        return Ok(1);
    } else if number == 2 {
        return Ok(2);
    }
    let mut sum: BigUint = Zero::zero();
    let mut last: BigUint = Zero::zero();
    let mut curr: BigUint = One::one();

    for i in 1..number {
        sum = last + curr;
        last = curr;
        curr = sum;
    }
    Ok(sum)
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib_in_rust_recursive, m)?)?;
    m.add_function(wrap_pyfunction!(get_fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(get_fibonacci_big, m)?)?;
    Ok(())
}
