use std::collections::HashMap;
use std::fs;

fn main() {
    let input = get_test_input();
    let points = get_vec_of_points(input);
    let lines = get_lines(points);
    get_all_points(lines);

    let input = read_input("input.txt");
    let points = get_vec_of_points(input);
    let lines = get_lines(points);
    get_all_points(lines)
}

fn read_input(file: &str) -> String {
    let data = fs::read_to_string(file).expect("Unable to read file");
    data
}

fn get_all_points(lines: Vec<Line>) {
    let mut counter: HashMap<Point, i32> = HashMap::new();
    for line in lines {
        //println!(
        //   "line in lines\n{} {} {} {}",
        //    line.a.x, line.a.y, line.b.x, line.b.y
        //);
        let line_points = line.create_line();
        for point in line_points {
            *counter.entry(point).or_default() += 1
        }
    }
    //println!("result:\n{:#?}", counter);
    let mut answer = 0;
    for v in counter.values() {
        if *v > 1 {
            answer += 1;
        }
    }
    println!("answer {}", answer)
}
// code related to setup
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Point {
    x: i32,
    y: i32,
}

#[derive(Debug)]
pub struct Line {
    a: Point,
    b: Point,
}

impl Line {
    pub fn new(a: Point, b: Point) -> Line {
        Self { a: a, b: b }
    }

    pub fn create_line(&self) -> Vec<Point> {
        let mut points: Vec<Point> = vec![];
        if self.a.y == self.b.y {
            // horizontal
            if self.a.x < self.b.x {
                let start = self.a.x;
                let finish = self.b.x;
                for x in start..=finish {
                    //println!("draw horizontal x {} y {}", x, self.a.y);
                    points.push(Point::new(x, self.a.y))
                }
            } else {
                let start = self.b.x;
                let finish = self.a.x;
                for x in start..=finish {
                    //println!("draw horizontal x {} y {}", x, self.a.y);
                    points.push(Point::new(x, self.a.y))
                }
            }
        } else if self.a.x == self.b.x {
            // horizontal
            if self.a.y < self.b.y {
                let start = self.a.y;
                let finish = self.b.y;
                for y in start..=finish {
                    //println!("horizontal x {} y {}", x, self.a.y);
                    points.push(Point::new(self.a.x, y))
                }
            } else {
                let start = self.b.y;
                let finish = self.a.y;
                for y in start..=finish {
                    //println!("horizontal x {} y {}", x, self.a.y);
                    points.push(Point::new(self.a.x, y))
                }
            }
        }
        return points;
    }
}

impl Point {
    pub fn new(x: i32, y: i32) -> Self {
        Self { x: x, y: y }
    }
}

pub fn get_lines(input: Vec<Vec<Point>>) -> Vec<Line> {
    let mut lines: Vec<Line> = vec![];
    for line in input {
        let new_line: Line = Line::new(line[0].clone(), line[1].clone());
        lines.push(new_line);
    }
    println!("ALL LINES {:#?}", lines);
    lines
}

pub fn get_test_input() -> String {
    let input: String = String::from(
        "0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2",
    );
    input
}

fn get_vec_of_points(input_data: String) -> Vec<Vec<Point>> {
    let mut ret: Vec<Vec<Point>> = vec![];
    for line in input_data.lines() {
        let mut vec_of_points: Vec<Point> = vec![];
        for parts in line.split("->") {
            //println!("{}", parts);
            let v: Vec<&str> = parts.trim().split(",").collect();
            //println!("{:?}", v);
            let x = v[0].parse::<i32>().unwrap();
            let y = v[1].parse::<i32>().unwrap();
            let point: Point = Point::new(x, y);
            vec_of_points.push(point);
        }
        ret.push(vec_of_points);
    }
    println!("{:?}", ret);
    ret
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_vec_of_points() {
        let input = get_test_input();
        let points = get_vec_of_points(input);

        assert_eq!(points.len(), 10);
    }
    #[test]
    fn test_line_creation() {
        let pt_1: Point = Point::new(0, 9);
        let pt_2: Point = Point::new(5, 9);
        let line: Line = Line::new(pt_1, pt_2);
        println!("{:?}", line);
        assert_eq!(line.a.x, 0);
        assert_eq!(line.b.y, 9);
    }
}
