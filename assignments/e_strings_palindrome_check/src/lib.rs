use pyo3::prelude::*;

#[pyfunction]
fn is_palindrome_slow(string: String) -> bool {
    let string_reversed: String = string.chars().rev().collect();

    return string_reversed == string;
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(is_palindrome_slow, m)?)?;
    Ok(())
}
