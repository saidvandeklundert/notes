use crate::constants;
use std::error::Error;
use std::fs;

pub fn hello() {
    println!("Hello, let's play with files!")
}

// Read a file and return the content as a String:
pub fn read_file(file_path: &str) -> Result<String, Box<dyn Error>> {
    let contents = fs::read_to_string(file_path)?;

    Ok(contents)
}

pub fn run_all() {
    let file_content = read_file(constants::TEN).unwrap();
    println!("{}", file_content);
}
