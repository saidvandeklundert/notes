fn is_palindrome_slow(string: String) -> bool {
    let string_reversed: String = string.chars().rev().collect();

    return string_reversed == string;
}

fn main() {
    let example = "abcdcba".to_string();
    let example_rev: String = example.chars().rev().collect();
    let res = example_rev == example_rev;
    println!("{} {} {}", example, example_rev, res);

    println!("{}", is_palindrome_slow("abcdcba".to_string()));
}
