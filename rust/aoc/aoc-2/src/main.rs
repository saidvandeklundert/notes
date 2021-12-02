use std::fs::File;
use std::io;
use std::io::prelude::*;

fn main() {
    {
        //1
        let mut point = Point::new(0, 0);
        println!("{:?}", point);
        let input = read_input();
        for (instruction, value) in input {
            match instruction.as_ref() {
                "forward" => point.forward(value),
                "down" => point.down(value),
                "up" => point.up(value),
                _ => println!("nothing"),
            }
        }
        println!("{:?}", point);
        #[derive(Debug, Copy, Clone)]
        pub struct Point {
            x: i32,
            y: i32,
        }

        impl Point {
            pub fn new(x: i32, y: i32) -> Point {
                Self { x: x, y: y }
            }

            pub fn forward(&mut self, x: i32) {
                self.x += x;
            }

            pub fn up(&mut self, y: i32) {
                self.y -= y;
            }
            pub fn down(&mut self, y: i32) {
                self.y += y;
            }
        }
    }
    {
        //2
        let mut point = Point::new(0, 0, 0);
        println!("{:?}", point);
        let input = read_input();
        for (instruction, value) in input {
            match instruction.as_ref() {
                "forward" => point.forward(value),
                "down" => point.down(value),
                "up" => point.up(value),
                _ => println!("nothing"),
            }
        }
        println!("{:?}", point);
        #[derive(Debug, Copy, Clone)]
        pub struct Point {
            horizontal: i32,
            depth: i32,
            aim: i32,
        }

        impl Point {
            pub fn new(x: i32, y: i32, z: i32) -> Point {
                Self {
                    horizontal: x,
                    depth: y,
                    aim: z,
                }
            }

            pub fn forward(&mut self, horizontal: i32) {
                self.horizontal += horizontal;
                let increase: i32 = self.aim * horizontal;
                self.depth += increase;
            }

            pub fn up(&mut self, depth: i32) {
                self.aim -= depth;
            }
            pub fn down(&mut self, depth: i32) {
                self.aim += depth;
            }
        }
    }
}

type Movement = (String, i32);

fn read_input() -> Vec<Movement> {
    let mut vec: Vec<Movement> = vec![];
    let file = File::open("input.txt").unwrap();
    let reader = io::BufReader::new(file);
    for line in reader.lines() {
        let line = line.unwrap();
        let mut iter = line.split_whitespace();
        let movement: &str = iter.next().unwrap();
        let value: i32 = iter.next().unwrap().parse::<i32>().unwrap();
        //println!("{} {}", movement, value);
        let movement_tuple: Movement = (movement.to_string(), value);
        vec.push(movement_tuple);
    }
    //println!("{:?}", vec);
    vec
}
