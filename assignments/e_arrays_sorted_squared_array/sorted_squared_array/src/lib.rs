use pyo3::prelude::*;

/// Multiply two numbers:
#[pyfunction]
fn sorted_squared_array(a: isize, b: isize) -> PyResult<isize> {
    Ok(a * b)
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ssa(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sorted_squared_array, m)?)?;
    Ok(())
}
