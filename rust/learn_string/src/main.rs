use std::fmt;
use std::slice;
use std::str;
/*

*/
fn main() {
    // From https://doc.rust-lang.org/std/primitive.str.html#representation
    let story = "Once upon a time...";
    let ptr = story.as_ptr();
    let len = story.len();
    // story, a '&str', has nineteen bytes
    assert_eq!(19, len);
    // We can re-build a str out of ptr and len. This is all unsafe because
    // we are responsible for making sure the two components are valid:
    let s = unsafe {
        // First, we build a &[u8]...
        let slice = slice::from_raw_parts(ptr, len);
        // ... and then convert that slice into a string slice
        str::from_utf8(slice)
    };
    assert_eq!(s, Ok(story));
    println!("{:#?}\n{:#?}", story, s);

    // My addition:
    unsafe {
        // we can build a &[u8] from the pointer and the lenght
        let byteslice = slice::from_raw_parts(ptr, len);
        // we can take the byteslice and transform it into a vec:
        let new_string = String::from_utf8_unchecked(byteslice.to_vec());
        println!(" byteslice {}", new_string);
        // We can transmute the created String into a different struct
        // with the same layout and then access the vec:
        let mut string_exposed: MyString = std::mem::transmute(new_string);
        println!("{:#?}", string_exposed.vec);
        string_exposed.push_str("adding this to the string value");
        println!("{:#?}", string_exposed.vec);
        // We can also transmute it back into String:
        let string_again: String = std::mem::transmute(string_exposed);
        println!("{}", string_again);
    }

    let mut newer_string = String::from("new");
    newer_string += " something added";
    println!("{}", newer_string);
    {
        let string: String = String::from("This is a string.");
        println!("{}", string);
    }
    {
        let string: String = String::with_capacity(20);
        println!(
            "string:{}\n len: {} cap: {}",
            string,
            string.len(),
            string.capacity()
        );
    }
    {
        let mut string: String = String::new();
        println!(
            "string:{}\n len: {} cap: {}",
            string,
            string.len(),
            string.capacity()
        );
        string.push_str("string");
        println!(
            "string:{}\n len: {} cap: {}",
            string,
            string.len(),
            string.capacity()
        );
    }
    {
        use std::mem;
        let s1 = String::from("abcdefghijklmnopqrstuvwyxz");
        let s2 = String::from(".");
        s1.is_alpha();
        s2.is_alpha();
        println!("{} {}", s1.is_alpha(), s2.is_alpha());

        let str_1 = "abcdefghijklmnopqrstuvwyxz";
        let str_2 = ".";
        println!("{} {}", str_1.is_alpha(), str_2.is_alpha());
        println!("{}", mem::size_of::<MyString>());
    }
    {
        use core::mem::{self, ManuallyDrop, MaybeUninit};
        let mut string: String = String::from("some string");
        let another_string: String = String::from(" and another string");
        let yet_another_string: &str = " and another string";
        string.extend(another_string.chars());
        string.extend(yet_another_string.chars());
        println!("{}", string);
    }
}

// Alternative string
pub struct MyString {
    pub vec: Vec<u8>,
}
impl MyString {
    // Copied straight from the std, method that is defined for String
    pub fn push_str(&mut self, string: &str) {
        self.vec.extend_from_slice(string.as_bytes())
    }
}

pub trait Stringer {
    fn is_alpha(&self) -> bool;
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
}

impl Stringer for &str {
    fn is_alpha(&self) -> bool {
        for c in self.chars() {
            if !c.is_alphabetic() {
                return false;
            }
        }
        return true;
    }
}

//

/*
impl String{
    #[stable(feature = "rust1", since = "1.0.0")]
    pub fn pop(&mut self) -> Option<char> {
        let ch = self.chars().rev().next()?;
        let newlen = self.len() - ch.len_utf8();
        unsafe {
            self.vec.set_len(newlen);
        }
        Some(ch)
    }


    #[stable(feature = "rust1", since = "1.0.0")]
    pub fn clear(&mut self) {
        self.vec.clear()
    }
}

#[cfg(not(no_global_oom_handling))]
#[stable(feature = "rust1", since = "1.0.0")]
impl Clone for String {
    fn clone(&self) -> Self {
        String { vec: self.vec.clone() }
    }

    fn clone_from(&mut self, source: &Self) {
        self.vec.clone_from(&source.vec);
    }
}

#[cfg(not(no_global_oom_handling))]
#[stable(feature = "rust1", since = "1.0.0")]
impl FromIterator<char> for String {
    fn from_iter<I: IntoIterator<Item = char>>(iter: I) -> String {
        let mut buf = String::new();
        buf.extend(iter);
        buf
    }
}



#[cfg(not(no_global_oom_handling))]
#[stable(feature = "str_to_string_specialization", since = "1.9.0")]
impl ToString for str {
    #[inline]
    fn to_string(&self) -> String {
        String::from(self)
    }
}
*/
