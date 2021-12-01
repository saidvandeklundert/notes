fn main() {
    {
        let number = 13;
        // TODO ^ Try different values for `number`
        println!("Tell me about {}", number);
        match number {
            // Match a single value
            1 => println!("One!"),
            // Match several values
            2 | 3 | 5 | 7 | 11 => println!("This is a prime"),
            // TODO ^ Try adding 13 to the list of prime values
            // Match an inclusive range
            13..=19 => println!("A teen"),
            // Handle the rest of cases
            _ => println!("Ain't special"),
            // TODO ^ Try commenting out this catch-all arm
        }
        let result = match number {
            1 => "one",
            2 | 3 => "2 or 3 ",
            4..=10 => "4 through 10",
            _ => "catchall",
        };
        println!("result: {}", result);
        let boolean = false;
        // Match is an expression too
        let binary = match boolean {
            // The arms of a match must cover all the possible values
            false => 0,
            true => 1,
            // TODO ^ Try commenting out one of these arms
        };

        println!("{} -> {}", boolean, binary);
    }
    {
        // logical
        let a = true;
        let b = false;
        let c = !a; //false
        let d = a && b; //false
        let e = a || b; //true
        println!("{} {} {}", c, d, e)
    }
    {
        // bitwise operators
        let a = 1;
        let b = 2;

        let c = a & b; //0  (01 && 10 -> 00)
        let d = a | b; //3  (01 || 10 -> 11)
        let e = a ^ b; //3  (01 != 10 -> 11)
        let f = a << b; //4  (Add b number of 0s to the end of a -> '01'+'00' -> 100)
        let g = a >> b; //0  (Remove b number of bits from the end of a -> o̶1̶ -> 0)
        println!("{}\n{}\n{}\n{}\n{}\n", c, d, e, f, g)
    }
}
