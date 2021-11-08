use pyo3::prelude::*;

#[pyfunction]
fn sorted_squared_array(vec: Vec<isize>) -> PyResult<Vec<isize>> {
    let mut new_vec: Vec<isize> = Vec::new();

    for nr in vec {
        let square: isize = nr * nr;
        new_vec.push(square);
    }
    new_vec.sort();
    Ok(new_vec)
}

#[pyfunction]
fn sorted_squared_array_optimized(vec: Vec<isize>) -> PyResult<Vec<isize>> {
    let mut new_vec: Vec<isize> = Vec::new();

    let mut start_index = 0;
    let mut end_index = vec.len() - 1;

    for (idx, value) in vec.iter().enumerate().rev() {
        println!("{} {}", idx, value)
    }
    Ok(new_vec)
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ssa(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sorted_squared_array, m)?)?;
    Ok(())
}
