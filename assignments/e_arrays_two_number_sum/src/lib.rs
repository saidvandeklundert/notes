use pyo3::prelude::*;
use std::collections::HashMap;

#[pyfunction]
fn two_number_sum(mut array: Vec<i32>, targetSum: i32) -> PyResult<Vec<i32>> {
    let mut seen: HashMap<i32, bool> = HashMap::new();
    let top = array.pop().unwrap();
    seen.insert(top, true);
    for v in array {
        let leftover = targetSum - v;
        if seen.contains_key(&leftover) {
            return Ok(vec![v, leftover]);
        } else {
            seen.insert(v, true);
        }
    }
    Ok(vec![])
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(two_number_sum, m)?)?;
    Ok(())
}
