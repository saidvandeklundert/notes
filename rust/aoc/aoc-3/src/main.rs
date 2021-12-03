use std::fs;
fn main() {
    {
        {
            let mut byte: u8 = 0b0000_0000;
            println!("1: 0b{:08b}", byte);
            byte |= 0b0000_1000; // Set a bit
            println!("2: 0b{:08b}", byte);
            byte &= 0b1111_0111; // Unset a bit
            println!("3: 0b{:08b}", byte);
            byte ^= 0b0000_1000; // Toggle a bit
            println!("4: 0b{:08b}", byte);
        }
        {
            let mut two_byte: u16 = 0b0000_0000_0000_0000;

            let epsilon = vec![0, 1, 0, 0, 1];
            let result = generate_4_bytes_number(epsilon);
            println!("4: 0b{:16b}", result);
            println!("{}", result);
        }
        //1 pathetic first attempt at a solution but it works:
        let data = input();
        println!("{:?}", data);
        // build a vec that is used to count all 0's
        let mut counter: Vec<usize> = vec![0; data[0].len()];
        println!("{:?}", counter);
        // count the 0's:
        for vec in &data {
            for (idx, value) in vec.iter().enumerate() {
                if *value == 0 {
                    counter[idx] += 1
                }
            }
        }
        println!("{:?}", counter);
        // set the most common bit by comparing the number of 0's
        // to the total amount of numbers:
        let numbers: usize = data.len();
        for v in counter.iter_mut() {
            let number_of_ones = numbers - *v;
            if number_of_ones > *v {
                *v = 1;
            } else {
                *v = 0;
            }
        }
        // define the gama as a vec in usize and epsilon as a vec in usize:
        let gamma: Vec<usize> = counter.clone();
        let epsilon: Vec<usize> = counter.into_iter().map(|x| zero_and_one_swap(x)).collect();
        println!("gamma {:?}", gamma);
        println!("epsilon {:?}", epsilon);

        let gamma_number = generate_4_bytes_number(gamma);
        let epsilon_number = generate_4_bytes_number(epsilon);
        println!("gamma_number {:?}", gamma_number);
        println!("epsilon_number {:?}", epsilon_number);
        let result = gamma_number * epsilon_number;
        println!("result {}", result);
    }
}

fn generate_4_bytes_number(vec: Vec<usize>) -> u32 {
    let mut f_bytes: u32 = 0b0000_0000_0000_0000_0000_0000_0000_0000;
    for (idx, v) in vec.iter().rev().enumerate() {
        // take the value of the element in the vec:
        let value = *v as u32;
        // set the bit number we are working with:
        let bit_nr = idx as u32;
        println!("value: {} bit_nr{}", value, bit_nr);
        // manipulate the n-th bit in the two_byte value:
        f_bytes |= value << bit_nr;
    }
    f_bytes
}

fn zero_and_one_swap(x: usize) -> usize {
    if x == 1 {
        0
    } else if x == 0 {
        1
    } else {
        panic!();
    }
}

fn input_string() -> String {
    let string: String = fs::read_to_string("input.txt").unwrap();
    string.trim().to_string()
}
fn input() -> Vec<Vec<u8>> {
    let mut vec: Vec<Vec<u8>> = Vec::new();
    let string = input_string();
    for line in string.lines() {
        println!("{}", line);
        let mut vec_to_add: Vec<u8> = vec![];
        for c in line.chars() {
            let addition = (c.to_string()).parse::<u8>().unwrap();
            vec_to_add.push(addition);
        }
        println!("{:?}", vec_to_add);
        vec.push(vec_to_add);
    }
    vec
}
