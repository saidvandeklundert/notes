#![feature(drain_filter)]
use std::fs;
use std::io::{prelude::*, BufReader};
const WIDTH: usize = 12;
fn main() {
    {
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
    {
        // assignment number 2:
        part_2();
        alt2();
    }
}

fn drop_uninteresting(vec_of_vec: &mut Vec<Vec<u8>>, idx: usize, keep: u8) {
    let mut to_drop: Vec<usize> = vec![];
    for (index, vec) in vec_of_vec.iter().enumerate() {
        if vec[idx] != keep {
            to_drop.push(index);
        }
    }

    for v in to_drop.iter().rev() {
        vec_of_vec.remove(*v);
    }
}
fn get_most_common_number(vec_of_vec: Vec<Vec<u8>>, idx: usize) -> u8 {
    let mut number_of_zeros = 0;
    let mut number_of_ones = 0;
    for vec in &vec_of_vec {
        if vec[idx] == 0 {
            number_of_zeros += 1
        } else if vec[idx] == 1 {
            number_of_ones += 1
        }
    }
    if number_of_zeros > number_of_ones {
        return 0;
    } else if number_of_ones > number_of_zeros {
        return 1;
    // when things are equal, return 0
    } else {
        return 1;
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
    let _string: String = fs::read_to_string("input.txt").unwrap();
    let string: String = String::from(
        "
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010",
    );
    string.trim().to_string()
}
fn input() -> Vec<Vec<u8>> {
    let mut vec: Vec<Vec<u8>> = Vec::new();
    let string = input_string();
    for line in string.lines() {
        let mut vec_to_add: Vec<u8> = vec![];
        for c in line.chars() {
            let addition = (c.to_string()).parse::<u8>().unwrap();
            vec_to_add.push(addition);
        }
        vec.push(vec_to_add);
    }
    vec
}

fn part_2() {
    let ls: Vec<Vec<char>> = BufReader::new(fs::File::open("input.txt").unwrap())
        .lines()
        .map(|l| l.unwrap().chars().collect())
        .collect();
    println!("part_2\nls first 2 elements:\n {:?}", &ls[0..2]);
    let mut vec_vec_char = ls.clone();

    for bit in 0..ls[0].len() {
        println!("bit: {:?}", bit);
        let bits = vec_vec_char.iter().map(|x| x[bit]).collect::<Vec<_>>();

        let c0 = bits.iter().filter(|x| **x == '0').count();
        let c1 = bits.iter().filter(|x| **x == '1').count();

        let keep = if c1 >= c0 { '1' } else { '0' };

        vec_vec_char.retain(|x| x[bit] == keep);
        if vec_vec_char.len() == 1 {
            break;
        }
    }

    let mut nums_car = ls.clone();

    for bit in 0..ls[0].len() {
        let bits = nums_car.iter().map(|x| x[bit]).collect::<Vec<_>>();

        let c0 = bits.iter().filter(|x| **x == '0').count();
        let c1 = bits.iter().filter(|x| **x == '1').count();

        let keep = if c1 >= c0 { '0' } else { '1' };

        nums_car.retain(|x| x[bit] == keep);
        if nums_car.len() == 1 {
            break;
        }
    }

    let oxy = u32::from_str_radix(&vec_vec_char[0].iter().collect::<String>(), 2).unwrap();
    let car = u32::from_str_radix(&nums_car[0].iter().collect::<String>(), 2).unwrap();

    println!("part 2 : {:?}", oxy * car);
}
pub fn alt2() {
    //https://github.com/timvisee/advent-of-code-2021/blob/master/day03b/src/main.rs
    let nums = include_str!("input.txt")
        .lines()
        .map(|l| u32::from_str_radix(l, 2).unwrap())
        .collect::<Vec<_>>();

    let oxy = (0..WIDTH)
        .rev()
        .scan(nums.clone(), |oxy, i| {
            let one = oxy.iter().filter(|n| *n & 1 << i > 0).count() >= (oxy.len() + 1) / 2;
            oxy.drain_filter(|n| (*n & 1 << i > 0) != one);
            oxy.first().copied()
        })
        .last()
        .unwrap();

    let co2 = (0..WIDTH)
        .rev()
        .scan(nums, |co2, i| {
            let one = co2.iter().filter(|n| *n & 1 << i > 0).count() >= (co2.len() + 1) / 2;
            co2.drain_filter(|n| (*n & 1 << i > 0) == one);
            co2.first().copied()
        })
        .last()
        .unwrap();

    println!("{}", oxy * co2);
}
/*
        {
            // these are just notes
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
            // these are just notes
            let two_byte: u16 = 0b0000_0000_0000_0000;

            let epsilon = vec![0, 1, 0, 0, 1];
            let result = generate_4_bytes_number(epsilon);
            println!("4: 0b{:16b}", result);
            println!("{}", result);
        }
*/
