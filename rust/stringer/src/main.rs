use stringer;
use stringer::Stringer;
fn main() {
    let input_str = "Sushi is the best!";
    let res = stringer::reverse_words(input_str);
    println!("{}\n{}", input_str, res);
    let res_2 = stringer::count_char(input_str, 'e');
    println!("{}", res_2);
    let res_2 = stringer::count_char_case_sensitive(input_str, 'e');
    println!("{}", res_2);

    let s1: String = String::from("Example");
    let mut s2: String = String::from("Sushi is the best!");
    let s3: &str = "Working from home it the best!";
    let mut s4: String = String::from("Another example. Word, word, word, word.");
    println!(
        "is_alpha:\n{}\n{}\n{}",
        s1.is_alpha(),
        s2.is_alpha(),
        s3.is_alpha()
    );
    s2.reverse_words();
    println!("reverse_words:\n{}", s2);
    println!("reverse_words:\n{}", s2);
    let res = s4.count_word("word");
    println!("count_word res:\n{}", res);
    s2.r_strip_word_alpha();
    println!("r_strip_word_alpha {}", s2);

    let s1: String = String::from("Example.");
    let s2: String = String::from("Example.Example.Example.Example.\nExaMple.!>(*^*%example.");
    let s3: String = String::from("Some random text.");
    println!("{}", s1.count_word("example"));
    // work on count_word
}
