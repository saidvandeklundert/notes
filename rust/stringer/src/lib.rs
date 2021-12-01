// Reverse the words in a string
pub fn reverse_words(input_str: &str) -> String {
    let mut reversed_str = String::new();
    let mut words = input_str.split_whitespace();
    while let Some(word_to_add) = words.next_back() {
        reversed_str.push_str(word_to_add);
        reversed_str.push(' ');
    }
    reversed_str
}

// Count target char in a string and return the count. Does not
// care about case:
pub fn count_char(input_str: &str, target_char: char) -> usize {
    let mut count = 0;
    for c in input_str.chars() {
        if target_char == c.to_lowercase().next().unwrap() {
            count += 1;
        }
    }
    count
}

// Count target char in a string and return the count. Does care about case:
pub fn count_char_case_sensitive(input_str: &str, target_char: char) -> usize {
    let mut count = 0;
    for c in input_str.chars() {
        if target_char == c {
            count += 1;
        }
    }
    count
}

// Counts the occurence of target word in a string.
// Punctuation does not play a role in the search.
pub fn count_word(input_str: &str, target_word: &str) -> usize {
    let mut count = 0;

    let words = input_str.split_whitespace();

    for word in words {
        if word == target_word {
            count += 1;
        }
    }
    count
}

// Convenience functions related to strings.
pub trait Stringer {
    fn is_alpha(&self) -> bool;
    fn make_alpha(&mut self);
    fn r_strip_word_alpha(&mut self);
    fn reverse_words(&mut self);
    fn count_word(&self, target_word: &str) -> usize;
}

impl Stringer for String {
    fn is_alpha(&self) -> bool {
        for c in self.chars() {
            if !c.is_alphabetic() {
                return false;
            }
        }
        return true;
    }
    fn make_alpha(&mut self) {
        let mut new_string: String = String::with_capacity(self.len());
        for c in self.chars() {
            if c.is_alphabetic() {
                new_string.push(c)
            }
        }
        self.clear();
        self.push_str(&new_string);
    }

    // Remove trailing non-aphabetic characters from a word.
    // Removes all text from string in case a multiword text is given.
    fn r_strip_word_alpha(&mut self) {
        let mut new_string: String = String::with_capacity(self.len());
        let mut remove = false;
        for c in self.chars() {
            if remove == false {
                if !c.is_alphabetic() {
                    remove = true;
                } else {
                    new_string.push(c);
                }
            } else {
                break;
            }
        }
        self.clear();
        self.push_str(&new_string);
    }

    fn reverse_words(&mut self) {
        let mut reversed_str = String::with_capacity(self.len());
        let mut words = self.split_whitespace();
        while let Some(word_to_add) = words.next_back() {
            reversed_str.push_str(word_to_add);
            reversed_str.push(' ');
        }
        self.clear();
        self.push_str(&reversed_str);
    }
    // Returns the count for target word in self.
    fn count_word(&self, target_word: &str) -> usize {
        let mut count: usize = 0;
        let words = self.split_whitespace();

        for word in words {
            word.to_string().r_strip_word_alpha();
            println!(
                "\tcount_word:\n{}\ntarget-{}",
                word.to_lowercase(),
                target_word
            );
            if word == target_word {
                println!(
                    "\tcount_word-{} target-{} are the same",
                    word.to_lowercase(),
                    target_word
                );
                count += 1
            }
        }
        return count;
    }
}

impl Stringer for &str {
    // Checks if all the characters in a String/str are alphabetic characters.
    // Retruns true if all characters are alphabetic, false otherwise.
    fn is_alpha(&self) -> bool {
        for c in self.chars() {
            if !c.is_alphabetic() {
                return false;
            }
        }
        return true;
    }
    fn make_alpha(&mut self) {
        return;
    }
    fn r_strip_word_alpha(&mut self) {
        return;
    }
    fn reverse_words(&mut self) {
        return;
    }
    fn count_word(&self, target_word: &str) -> usize {
        let mut count: usize = 0;

        let words = self.split_whitespace();

        for word in words {
            if word == target_word {
                count += 1
            }
        }
        return count;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_alpha() {
        let s1: String = String::from("Example");
        let s2: String = String::from("Sushi is the best!");

        assert_eq!(s1.is_alpha(), true);
        assert_eq!(s2.is_alpha(), false);
    }

    #[test]
    fn test_make_alpha() {
        let mut s1: String = String::from("Example");
        let mut s2: String = String::from("Sushi is the best!");
        s1.make_alpha();
        s2.make_alpha();
        assert_eq!(s1, "Example");
        assert_eq!(s2, "Sushiisthebest");
    }

    #[test]
    fn test_r_strip_word_alpha() {
        let mut s1: String = String::from("Example.");
        let mut s2: String = String::from("Sushi is the best!");
        let mut s3: String = String::from("Example");
        s1.r_strip_word_alpha();
        s2.r_strip_word_alpha();
        s3.r_strip_word_alpha();
        assert_eq!(s1, "Example");
        assert_eq!(s2, "Sushi");
        assert_eq!(s3, "Example");
    }

    /*
    #[test]
    fn test_count_word() {
        let s1: String = String::from("Example.");
        let s2: String = String::from("Example.Example.Example.Example.\nExaMple.!>(*^*%example.");
        let s3: String = String::from("Some random text.");
        assert_eq!(1, s1.count_word("example"));
        assert_eq!(6, s2.count_word("example"));
        assert_eq!(0, s3.count_word("example"));
    }*/
}
