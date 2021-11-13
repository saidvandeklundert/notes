use pyo3::prelude::*;

#[pyfunction]
fn fib_in_rust_recursive(n: u32) -> PyResult<u32> {
    println!("{}", n);
    Ok(get_nth_fib(n))
}

fn get_nth_fib(number: u32) -> u32 {
    match number {
        1 => return number,
        2 => return number,
        _ => return get_nth_fib(number - 1) + get_nth_fib(number - 2),
    }
}

fn get_fibonacci(number: u32) -> PyResult<u32> {
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

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib_in_rust_recursive, m)?)?;
    m.add_function(wrap_pyfunction!(get_fibonacci, m)?)?;
    Ok(())
}
