use std::collections::HashMap;
use std::fs::File;
use std::io::BufReader;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::{Duration, Instant};

//r"C:\dev-container\python\rust\counting_characters\random.txt"
pub fn main() {
    let start = Instant::now();
    let mut char_map: HashMap<char, u128> = HashMap::new();
    let mut f = BufReader::new(File::open(r"/var/tmp/random.txt").expect("open failed"));
    for line in f.lines() {
        for c in line.expect("lines failed").chars() {
            if char_map.contains_key(&c) {
                let value = char_map.get_mut(&c).unwrap();
                *value += 1;
            } else {
                char_map.insert(c, 1);
            }
        }
    }
    println!("{:?}", char_map);
    println!("Time spend creating the char map: {:?}", start.elapsed());
}
