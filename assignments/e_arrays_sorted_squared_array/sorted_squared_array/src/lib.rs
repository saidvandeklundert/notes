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
    let mut new_vec: Vec<isize> = vec![0; vec.len()];

    let mut start_index = 0;
    let mut end_index = vec.len() - 1;

    for (idx, _) in vec.iter().enumerate().rev() {
        //println!("{} {}", idx, value);
        let start_v = vec[start_index];
        let end_v = vec[end_index];
        if start_v.abs() > end_v.abs() {
            new_vec[idx] = start_v * start_v;
            start_index += 1
        } else {
            new_vec[idx] = end_v * end_v;
            end_index += 1
        }
    }
    Ok(new_vec)
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ssa(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sorted_squared_array, m)?)?;
    m.add_function(wrap_pyfunction!(sorted_squared_array_optimized, m)?)?;
    Ok(())
}
