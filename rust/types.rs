#![allow(unused_variables, dead_code)]

fn main() {
    /*
    Types:
    https://doc.rust-lang.org/reference/types.html
    Scalar types:
      - booleans
      - characters
      - integers
      - floats
    */

    //Scalar types
    let ch: char = 'z';
    let b: bool = true;
    let e: i32 = -2_323; // underscore is ignore, used to improve readability
    let float: f32 = 3.4;
    println!(
        "char: {:?}\nbool: {:?}\ni32: {:?}\nfloat32: {:?}\n",
        ch, b, e, float
    );
    // integers can be 'annotated':
    let c = 30i32;
    let d = 30_i32; // the _ is ignored by the compiler, it can help improve readability
    println!("annotated i32: {:?}\nanother annotated i32: {:?}\n", c, d);
    /*
        sequences:
        - Tuple - heterogeneous, can hold different types
        - Array - homogeneous, can hold 1 type only and cannot change size.
        - Slice - view into a block of memory represented as a pointer and a length
    */
    // Tuple:
    let tuple: (f32, f32) = (6.35, 15.123);
    println!(
        "tuple: {:?}\ntuple, element 0: {:?}\ntuple, element 1: {:?}",
        tuple, tuple.0, tuple.1
    );
    // Array:
    let arr: [u8; 2] = [12, 233];
    println!("array: {:?}\narray, element 1: {:?}", arr, arr[1]);
    //Slice:
    let s = String::from("hello world");
    let hello = &s[0..5];
    let world = &s[6..11];
    assert_eq!(hello, "hello");
    assert_eq!(world, "world");
    /*
        User-defined types:
        - Struct
        - Enum
        - Union
    */
    // Structs:
    // 'Classic' struct:
    struct Server {
        name: String,
        ipv4: String,
        uptime: i32,
    }
    let s1 = Server {
        name: String::from("RustyBeak"),
        ipv4: String::from("1.1.1.1"),
        uptime: 123124,
    };
    assert_eq!(s1.name, "RustyBeak");
    assert_eq!(s1.ipv4, "1.1.1.1");
    assert_eq!(s1.uptime, 123124);
    // Named Tuple struct:
    struct StructTuple(String, bool);
    let named_tuple = StructTuple(String::from("example"), true);
    assert_eq!(named_tuple.0, "example");
    assert_eq!(named_tuple.1, true);
    //Unit struct
    #[derive(Debug)]
    struct UnitStruct;
    let unit_struct = UnitStruct;
    let message = format!("{:?}s are fun!", unit_struct);
    assert_eq!(message, "UnitStructs are fun!");

    // Classic struct and implementation of a function:
    struct Person {
        name: String,
        age: i32,
    }
    impl Person {
        fn introduce_self(&self) {
            println!(
                "Hi, my name is {} and I am {} years old.",
                self.name, self.age
            )
        }
    }
    let marie = Person {
        name: String::from("Marie"),
        age: 2,
    };
    marie.introduce_self();

    // Enum:
    /*
    An enum is always one and only one of those variants. If a struct wanted the same behavior, it would have to carefully enforce it and keep its fields private.
    Structs are equivalent to an "AND" combination of the individual fields, while enums are an "OR" combinator.
    */
    enum Color {
        Red,
        Green,
        Blue,
    }
    fn color_matcher(c: Color) {
        match c {
            Color::Red => println!("Color is Red!"),
            Color::Green => println!("Color is Green!"),
            _ => println!("Collor is not Red!"), // catch all in the match
        }
    }
    let c1: Color = Color::Red;
    let c2: Color = Color::Green;
    let c3: Color = Color::Blue;
    color_matcher(c1);
    color_matcher(c2);
    color_matcher(c3);

    // comprehensive enum with different variants
    #[derive(Debug)]
    enum Message {
        Move { x: i32, y: i32 }, // anonymous struct
        Echo(String),            // Variant with a single type of data
        ChangeColor(u8, u8, u8), // Variant with a tuple of data
        Quit,                    // Named variant with no data
    }
    impl Message {
        fn call(&self) {
            println!("{:?}", &self);
        }
    }
    let messages = [
        Message::Move { x: 10, y: 30 },
        Message::Echo(String::from("hello world")),
        Message::ChangeColor(200, 255, 255),
        Message::Quit,
    ];
    for message in &messages {
        message.call();
    }

    // Union:
    union IntOrFloat {
        i: i32,
        f: f32,
    }
    let mut iof = IntOrFloat { i: 123 };
    iof.i = 234;
    println!("iof.i = {}", unsafe { iof.i });

    /*
    Collections: https://doc.rust-lang.org/std/collections/index.html
    - Vector: A contiguous growable array type with heap-allocated contents.
        They can re-size, stores only 1 type of data
    */
    let mut a = vec![1, 2, 3]; // [1;10]
    a.push(4);
    println!("a = {:?}", a);
    let last_element = a.pop();
    println!("Last lement: {:?}", last_element);
    a.swap(0, 1);
    println!("a = {:?}", a);
    for x in &a {
        println!("{}", x);
    }
    let idx: usize = 2;
    println!("Use usize to access indexes: {}", a[idx]);
    //safe access to element:
    match a.get(10) {
        Some(x) => println!("a[6] = {}", x),
        None => println!("error, no such element"),
    }
    // when declaring a vec! without values, you need to specify the type:
    let mut cities: Vec<&str> = Vec::new();
    cities.push("Breda");
    cities.push("Rotterdam");

    /*
    Strings, strings, strings and strings.
    The two most important types:
    - &str: stack allocated string slice, a view into a string
    - String: heap allocated pub struct
    The String is defined as follows:
    ---
    pub struct String {
    vec: Vec<u8>,           // vector of 8-bit unsigned integers
    }
    ---
    &str:
    - inflexible
    - allocated on the stack
    - sequence of UTF-8 characters
    - you index into the bytes, not the char
    String:
    - flexible, can be modified
    - allocated on the heap
    - sequence of UTF-8 characters
    - you index into the bytes, not the char
    */
    let s = "Hello world!"; // &str

    // .chars() to iterate the characters
    for c in s.chars() {
        println!("{}", c);
    }

    let mut string = String::new(); // String
    let mut a = 'a' as u8;
    while a <= ('z' as u8) {
        string.push(a as char);
        string.push_str(",");
        a += 1;
    }
    println!("{}", string);

    // String to &str:
    let u: &str = &string;
    println!("u is {}", u);
    // &str to String:
    let v: String = s.to_string();
    println!("v is {}", v);
    // Create string from a string slice:
    let example_string: String = String::from("world.");
    let formatted = format!("Hello {}", example_string);
    println!("{}", formatted);

    /*
    Usefull snippets:
    */

    // Returning Error or OK in Result Enum:
    #[derive(PartialEq, Debug)]
    struct PositiveNonzeroInteger(u64);
    #[derive(PartialEq, Debug)]
    enum CreationError {
        Negative,
        Zero,
    }
    impl PositiveNonzeroInteger {
        fn new(value: i64) -> Result<PositiveNonzeroInteger, CreationError> {
            if value < 0 {
                return Err(CreationError::Negative);
            } else if value == 0 {
                return Err(CreationError::Zero);
            } else {
                return Ok(PositiveNonzeroInteger(value as u64));
            }
        }
    }
    assert!(PositiveNonzeroInteger::new(10).is_ok());
    assert_eq!(
        Err(CreationError::Negative),
        PositiveNonzeroInteger::new(-10)
    );
    assert_eq!(Err(CreationError::Zero), PositiveNonzeroInteger::new(0));

    // Dealing with type conversion:
    let tc_a: i32 = 12;
    let tc_b: f32 = 6.5;
    let tc_res: i32 = tc_a + tc_b as i32;
    println!("{}", tc_res);

    // Wrapping generics:
    #[derive(Debug, Copy, Clone)]
    struct Wrapper<T> {
        value: T,
    }
    impl<T> Wrapper<T> {
        pub fn new(value: T) -> Self {
            Wrapper { value }
        }
    }
    let w1 = Wrapper::new("Foo");
    let w2 = Wrapper::new(12);
    dbg!(w1);
    dbg!(w2);
    //
    let five = 0b101;
    dbg!(five);
    let thirty_one = 0x1F;
    dbg!(thirty_one);
    let two_hundred = 0o310;
    dbg!(two_hundred);

    /*
    Enhance types:
    #[derive(Debug)]
    #[derive(Debug,PartialEq)]
    */
}