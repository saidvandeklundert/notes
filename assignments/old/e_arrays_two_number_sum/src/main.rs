use std::collections::HashMap;

fn two_number_sum(mut array: Vec<i32>, targetSum: i32) -> Vec<i32> {
    let mut seen: HashMap<i32, bool> = HashMap::new();
    let top = array.pop().unwrap();
    seen.insert(top, true);
    for v in array {
        let leftover = targetSum - v;
        if seen.contains_key(&leftover) {
            return vec![v, leftover];
        } else {
            seen.insert(v, true);
        }
    }
    vec![]
}

fn main() {
    let res = two_number_sum(vec![3, 5, -4, 8, 11, 1, -1, 6], 10);
    println!("{:?}", res);
    let mut example: HashMap<i32, bool> = HashMap::new();
    example.insert(12, true);
    example.contains_key(&200);
}
