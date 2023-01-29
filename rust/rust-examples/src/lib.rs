pub mod constants;
pub mod files;
use std::error::Error;
use std::fs::File;
use std::io::{self, BufRead, BufReader, Read};

pub const TEN: &str = "./tests/files/ten.txt";

pub fn run(expected_file: &str) -> String {
    // Extra work here due to lossy UTF
    let mut file = File::open(expected_file).unwrap();
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer).unwrap();
    let expected = String::from_utf8_lossy(&buffer);

    expected.to_string()
}

pub fn run_all() {
    files::hello();
}
