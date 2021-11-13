fn main() {
    println!("YOLO");
    println!("{}", get_nth_fib(2));
    println!("{}", get_nth_fib(4));
}

fn get_nth_fib(number: i32) -> i32 {
    match number {
        1 => return number,
        2 => return number,
        _ => return get_nth_fib(number - 1) + get_nth_fib(number - 2),
    }
}
