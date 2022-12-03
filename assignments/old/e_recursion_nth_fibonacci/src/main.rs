fn main() {
    println!("YOLO");
    println!("{}", get_nth_fib(2));
    println!("{}", get_nth_fib(4));
    println!("{}", get_nth_fib(100));
}

fn get_nth_fib(number: u128) -> u128 {
    if number == 1 {
        return 1;
    } else if number == 2 {
        return 2;
    }

    let mut sum = 0;
    let mut last = 0;
    let mut curr = 1;
    for i in 1..number {
        sum = last + curr;
        last = curr;
        curr = sum;
    }
    sum
}
