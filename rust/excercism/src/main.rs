fn main() {
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
        let total = total();
        println!("{}", total);
        let x = 10;
        println!("{}", 1 << 1);
        println!("{}", 2 << 1);
        println!("{}", 3 << 1);
        println!("{}", 4 << 1);
        println!("{}", 1 >> 10);
    }
    {
        pub fn square(s: u32) -> u64 {
            match s {
                1..=64 => 1u64.wrapping_shl(s - 1),
                _ => panic!("Square must be between 1 and 64"),
            }
        }
        pub fn total() -> u64 {
            (1..65).map(square).sum()
        }
        let res = square(4);
        println!("square {}", res);
    }
    {
        pub fn series(digits: &str, len: usize) -> Vec<String> {
            let mut expected: Vec<String> = vec![];
            if len > digits.len() {
                // I thought you deserve whatever you get would be whatever is in digits.
                //res.push(digits.to_string());
                expected
            } else {
                let max = digits.len();
                let mut idx = 0;
                while (idx + len) <= max {
                    let string: String = digits.get(idx..(idx + len)).unwrap().to_string();
                    expected.push(string);
                    idx += 1
                }
                expected
            }
        }
        fn test_too_long() {
            let expected: Vec<String> = vec![];
            assert_eq!(series("92017", 6), expected);
        }
        let res = series("49142", 3);
        println!("{:?}", res);
        let res = series("92017", 2);
        println!("{:?}", res);
        let res = series("92017", 6);
        println!("{:?}", res);
        test_too_long()
    }
}
