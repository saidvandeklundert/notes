fn main() {
    let input_str = "AlgoExpert is the best!";

    let res = reverse_words(input_str);
    println!("{}\n{}", input_str, res);
}

fn reverse_words(input_str: &str) -> String {
    let mut reversed_str = String::new();
    let mut words = input_str.split_whitespace();
    while let Some(word_to_add) = words.next_back() {
        println!("char_to_add {}", word_to_add);
        reversed_str.push_str(word_to_add);
        reversed_str.push(' ');
    }
    reversed_str
}
fn reverse_words_og(input_str: &str) -> String {
    let mut reversed_str = String::new();
    let mut chars = input_str.split_whitespace();
    println!("words:\n{:#?}", chars);
    while let Some(char_to_add) = chars.next_back() {
        println!("char_to_add {}", char_to_add);
        reversed_str.push_str(char_to_add);
        if let Some(next_word) = chars.next_back() {
            reversed_str.push(' ');
        }
    }
    reversed_str
}
/*
def reverseWordsInString(string: str):
    words = []
    start_of_word = 0

    for idx in range(len(string)):
        char = string[idx]

        # this marks the end of a word, so we slice up untill the previous index:
        if char == " ":
            # this is a slice up to, but not including idx:
            #   l = [0,1,2]
            #   l[0:2]
            #   >>> [0,1] < the 2 here is missing!
            word = string[start_of_word:idx]
            print(f"appending word -{word}-")
            print("words now", words)
            words.append(word)
            start_of_word = idx
        # adding a space to the words list
        elif string[start_of_word] == " ":
            words.append(" ")
            start_of_word = idx
    words.append(string[start_of_word:])

    reverse_list(words)
    return "".join(words)


def reverse_list(a_list):
    start, end = 0, len(a_list) - 1
    while start < end:
        a_list[start], a_list[end] = a_list[end], a_list[start]
        start += 1
        end -= 1
*/
