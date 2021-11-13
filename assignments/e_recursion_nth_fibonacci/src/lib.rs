use pyo3::prelude::*;

#[pyfunction]
fn fib_in_rust(number: isize) -> PyResult<isize> {
    Ok(get_nth_fib(number))
}

fn get_nth_fib(number: isize) -> isize {
    match number {
        1 => return number,
        2 => return number,
        _ => return get_nth_fib(number - 1) + get_nth_fib(number - 2),
    }
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib_in_rust, m)?)?;
    Ok(())
}
