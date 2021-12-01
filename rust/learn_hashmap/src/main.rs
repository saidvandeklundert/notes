use std::collections::HashMap;
fn main() {
    println!("Hello, world!");
    // define the hashmap
    let mut hm: HashMap<String, String> = HashMap::new();
    let mut hm: HashMap<String, String> = HashMap::with_capacity(1200);
    // Insert key value into hashmap:
    hm.insert("key-1".to_string(), "value-1".to_string());
    hm.insert("key-2".to_string(), "value-2".to_string());
    hm.insert("key-3".to_string(), "value-3".to_string());
    // check the hashmap capacity:
    println!("{}", hm.capacity());

    for key in hm.keys() {
        println!("{}", key)
    }
    for value in hm.values() {
        println!("{}", value);
    }
    for (idx, value) in hm.values_mut().enumerate() {
        *value = format!("VALUE-{}", idx + 1);
        println!("{}", value);
    }

    for (key, value) in hm.iter() {
        println!("{} : {}", key, value);
    }

    println!("{}", hm.contains_key("key-3"));
    println!("{}", hm.contains_key("key-33"));
    println!("{}", hm.len());
    println!("{}", hm.is_empty());

    for (k, v) in hm.drain().take(1) {
        println!("- {} {}", k, v);
    }
    for (k, v) in hm.drain() {
        println!("- {} {}", k, v);
    }

    let mut vec = vec![0, 1, 2];
    for v in vec.drain(0..) {
        println!("vec: {}", v);
    }

    let mut map: HashMap<i32, i32> = (0..8).map(|x| (x, x)).collect();
    // to clear all values
    //map.clear();
    println!(
        "{}\n{:?}",
        map.get(&1).unwrap(),
        map.get_key_value(&1).unwrap(),
    );
    println!("{}", map.remove(&1).unwrap(),);

    let mut vec_keys: Vec<i32> = map.into_keys().collect();
    let map: HashMap<i32, i32> = (0..8).map(|x| (x, x)).collect();
    let mut vec_values: Vec<i32> = map.into_values().collect();
    println!("{:?} {:?}", vec_keys, vec_values);
    let mut map: HashMap<i32, i32> = (0..8).map(|x| (x, x)).collect();
    map.keys();
    map.entry(1).or_insert(11);
    map.entry(100).or_insert(222);
    println!("{:?}", map);

    // playing with map:
    let vec = vec![1, 2, 3, 4];
    let result: Vec<i32> = vec.iter().map(|n| n * 10).collect();
    println!("{:?}", result);
    let x: Vec<i32> = result.into_iter().rev().collect();
    println!("{:?}", x);
    {
        let mut vec = vec![1, 2, 3, 4];
        vec.reverse();

        let multiplied: Vec<i32> = vec.into_iter().map(|x| multiply(x)).collect();
        println!("{:?}", multiplied);
    }
    {
        // filter example
        let mut vec: Vec<i32> = vec![1, 2, 3, 4];
        let res: Vec<i32> = vec.into_iter().filter(|x| *x >= 3).collect();
        println!("{:?}", res);
    }
    {
        pub fn reverse(input: &str) -> String {
            let mut result: String = String::from("");
            for c in input.chars().rev() {
                result.push(c)
            }
            return result;
        }
        reverse("yolo");
    }
    {
        pub fn square(s: u32) -> u64 {
            if s < 1 || s > 64 {
                panic!("Square must be between 1 and 64");
            }
            let mut result: u64 = 1;
            let mut counter = s - 1;
            while counter > 0 {
                result = result * 2;
                counter -= 1
            }
            return result;
        }
        pub fn total() -> u64 {
            let mut sum: u64 = 0;
            for i in 1..=64 {
                sum += square(i);
            }
            sum
        }
        let res = square(4);
        println!("square {}", res);
        //total();
    }
}
fn multiply(x: i32) -> i32 {
    return x * 2;
}
