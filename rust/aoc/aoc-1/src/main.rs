use std::fs::File;
use std::io;
use std::io::prelude::*;

fn input_to_vec(filename: &str) -> io::Result<Vec<i32>> {
    let mut ret_vec: Vec<i32> = vec![];
    let file = File::open(&filename)?;
    let reader = io::BufReader::new(file);
    for line in reader.lines() {
        let line = line?;
        let vec_addition = line.trim().parse::<i32>();
        match vec_addition {
            Ok(v) => ret_vec.push(v),
            Err(e) => println!("{} is not a int", e),
        }
    }
    Ok(ret_vec)
}

fn main() {
    {
        {
            //1
            let vec: Vec<i32> = input_to_vec("input.txt").unwrap();
            let mut count: i32 = 0;
            let mut previous_value: i32 = 0;
            for value in vec.iter() {
                if previous_value == 0 {
                    previous_value = *value;
                } else {
                    if *value > previous_value {
                        count += 1;
                    }
                    previous_value = *value;
                }
            }
            println!("descended {} times", count);
        }
        {
            // 2
            let vec: Vec<i32> = input_to_vec("input.txt").unwrap();
            let mut count: i32 = 0;
            let mut previous_window: i32 = 0;
            let iterator = vec.windows(3);
            for value in iterator {
                let curr_window_value: i32 = value.iter().sum();
                if curr_window_value > previous_window && previous_window != 0 {
                    count += 1;
                }
                previous_window = curr_window_value
            }
            println!("window increases: {}", count);
        }
    }
}
