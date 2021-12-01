# String

The `String` is added to the Prelude. Because of this, you can use it everywhere without having to import it specifically. The import is done like so:

```rust
pub use crate::string::{String, ToString};
```

The std defines the string [here](https://github.com/rust-lang/rust/blob/master/library/alloc/src/string.rs).

The String in Rust is defined as follows:
```rust
pub struct String {
    vec: Vec<u8>,
}
```

It is a struct with 1 private field, called `vec`. This field is a Vector of 8-bit unsigned integers, or bytes.


## Creating a new String

- String::from()
- String::with_capacity()
- String::new()

### String::from()


When youWhen implementing `String::from()`, the std implemented a trait for String. It was implemented in `string.rs` as follows:

```rust
impl From<&str> for String {
    /// Converts a `&str` into a [`String`].
    ///
    /// The result is allocated on the heap.
    #[inline]
    fn from(s: &str) -> String {
        s.to_owned()
    }
}
```

This trait is specified [here](https://github.com/rust-lang/rust/blob/master/library/core/src/convert/mod.rs):

```rust
pub trait From<T>: Sized {
    /// Performs the conversion.
    #[lang = "from"]
    #[must_use]
    #[stable(feature = "rust1", since = "1.0.0")]
    fn from(_: T) -> Self;
}
```

In `string.rs`, this trait is implemented for a few types, these include:
- `&str`
- `&mut str`
- `&String`
- `Box<str>`.

There are some differences in the way the trait is implemented. For instance, when called on a `&str` or `&mut str`, `to_owned` is called on the `&str`, creating owned data from borrowed data. When called on `&String`, the `&String` is cloned and the clone is returned.

### String::with_capacity()

You can use `with_capacity` to create a new empty 'String' that has the vector set with a certain capacity:

```rust
impl String {
    pub fn with_capacity(capacity: usize) -> String {
        String { vec: Vec::with_capacity(capacity) }
    }
}
```

If you push additional characters onto a string, the vector will need to grow in size to be able to accomodate this.

The Vector fr
```rust
impl<T> Vec<T> {
    pub fn with_capacity(capacity: usize) -> Self {
        Self::with_capacity_in(capacity, Global)
    }
}
```

Growing the String:
```rust
impl String {
    pub fn push_str(&mut self, string: &str) {
        self.vec.extend_from_slice(string.as_bytes())
    }
}
```

Which is calling this on the Vector:
```rust
impl<T: Clone, A: Allocator> Vec<T, A> {
    pub fn extend_from_slice(&mut self, other: &[T]) {
        self.spec_extend(other.iter())
    }
}
```

### String::new()

This is using a 'standard' constructer:

```rust
impl String {
    pub const fn new() -> String {
        String { vec: Vec::new() }
    }
}
```

The `Vec::new()` will do the following:

```rust
impl<T> Vec<T> {
    ...
    pub const fn new() -> Self {
        Vec { buf: RawVec::NEW, len: 0 }
    }
}
```

So basically, `String::new()` will give us a `String` struct with a `vec` field that is zero-length vector.

## Things I noticed about Strings

```
/// `String` implements <code>[Deref]<Target = [str]></code>, and so inherits all of [`str`]'s
/// methods. In addition, this means that you can pass a `String` to a
/// function which takes a [`&str`] by using an ampersand (`&`):
///
/// ```
/// fn takes_str(s: &str) { }
///
/// let s = String::from("Hello");
///
/// takes_str(&s);
/// ```
```

```rust
    pub fn into_raw_parts(self) -> (*mut u8, usize, usize) {
        self.vec.into_raw_parts()
    }
```

```rust
    pub unsafe fn from_raw_parts(buf: *mut u8, length: usize, capacity: usize) -> String {
        unsafe { String { vec: Vec::from_raw_parts(buf, length, capacity) } }
    }
```


```rust
    pub fn into_bytes(self) -> Vec<u8> {
        self.vec
    }
```


```rust
    pub fn push_str(&mut self, string: &str) {
        self.vec.extend_from_slice(string.as_bytes())
    }

    pub fn push(&mut self, ch: char) {
        match ch.len_utf8() {
            1 => self.vec.push(ch as u8),
            _ => self.vec.extend_from_slice(ch.encode_utf8(&mut [0; 4]).as_bytes()),
        }
    }

    pub fn pop(&mut self) -> Option<char> {
        let ch = self.chars().rev().next()?;
        let newlen = self.len() - ch.len_utf8();
        unsafe {
            self.vec.set_len(newlen);
        }
        Some(ch)
    }
```

```rust
    pub fn capacity(&self) -> usize {
        self.vec.capacity()
    }

    pub fn len(&self) -> usize {
        self.vec.len()
    }    
```


```rust
    pub fn reserve(&mut self, additional: usize) {
        self.vec.reserve(additional)
    }
    pub fn reserve_exact(&mut self, additional: usize) {
        self.vec.reserve_exact(additional)
    }
    pub fn shrink_to_fit(&mut self) {
        self.vec.shrink_to_fit()
    }    
```    

```rust
    pub fn as_bytes(&self) -> &[u8] {
        &self.vec
    }
```

## Learning about traits by looking at String


## How clone is implemented:

```rust
impl Clone for String {
    fn clone(&self) -> Self {
        String { vec: self.vec.clone() }
    }

    fn clone_from(&mut self, source: &Self) {
        self.vec.clone_from(&source.vec);
    }
}
```

From `clone.rs`:

```rust
pub trait Clone: Sized {
    /// Returns a copy of the value.
    #[stable(feature = "rust1", since = "1.0.0")]
    #[must_use = "cloning is often expensive and is not expected to have side effects"]
    fn clone(&self) -> Self;


    #[stable(feature = "rust1", since = "1.0.0")]
    fn clone_from(&mut self, source: &Self) {
        *self = source.clone()
    }
}
```


From the vector ( `rust\library\alloc\src\vec\mod.rs`):
```rust
impl<T: Clone, A: Allocator + Clone> Clone for Vec<T, A> {
    #[cfg(not(test))]
    fn clone(&self) -> Self {
        let alloc = self.allocator().clone();
        <[T]>::to_vec_in(&**self, alloc)
    }

    // HACK(japaric): with cfg(test) the inherent `[T]::to_vec` method, which is
    // required for this method definition, is not available. Instead use the
    // `slice::to_vec`  function which is only available with cfg(test)
    // NB see the slice::hack module in slice.rs for more information
    #[cfg(test)]
    fn clone(&self) -> Self {
        let alloc = self.allocator().clone();
        crate::slice::to_vec(&**self, alloc)
    }

    fn clone_from(&mut self, other: &Self) {
        SpecCloneFrom::clone_from(self, other)
    }
}
```

## ToString

```rust
pub trait ToString {
    #[rustc_conversion_suggestion]
    #[stable(feature = "rust1", since = "1.0.0")]
    fn to_string(&self) -> String;
}
impl ToString for u8 {
    #[inline]
    fn to_string(&self) -> String {
        let mut buf = String::with_capacity(3);
        let mut n = *self;
        if n >= 10 {
            if n >= 100 {
                buf.push((b'0' + n / 100) as char);
                n %= 100;
            }
            buf.push((b'0' + n / 10) as char);
            n %= 10;
        }
        buf.push((b'0' + n) as char);
        buf
    }
}

impl ToString for i8 {
    #[inline]
    fn to_string(&self) -> String {
        let mut buf = String::with_capacity(4);
        if self.is_negative() {
            buf.push('-');
        }
        let mut n = self.unsigned_abs();
        if n >= 10 {
            if n >= 100 {
                buf.push('1');
                n -= 100;
            }
            buf.push((b'0' + n / 10) as char);
            n %= 10;
        }
        buf.push((b'0' + n) as char);
        buf
    }
}

impl ToString for str {
    #[inline]
    fn to_string(&self) -> String {
        String::from(self)
    }
}

impl ToString for Cow<'_, str> {
    #[inline]
    fn to_string(&self) -> String {
        self[..].to_owned()
    }
}

impl ToString for String {
    #[inline]
    fn to_string(&self) -> String {
        self.to_owned()
    }
}
```

## Extend:

```rust
impl Extend<String> for String {
    fn extend<I: IntoIterator<Item = String>>(&mut self, iter: I) {
        iter.into_iter().for_each(move |s| self.push_str(&s));
    }

    #[inline]
    fn extend_one(&mut self, s: String) {
        self.push_str(&s);
    }
}

impl<'a> Extend<&'a str> for String {
    fn extend<I: IntoIterator<Item = &'a str>>(&mut self, iter: I) {
        iter.into_iter().for_each(move |s| self.push_str(s));
    }

    #[inline]
    fn extend_one(&mut self, s: &'a str) {
        self.push_str(s);
    }
}

impl Extend<char> for String {
    fn extend<I: IntoIterator<Item = char>>(&mut self, iter: I) {
        let iterator = iter.into_iter();
        let (lower_bound, _) = iterator.size_hint();
        self.reserve(lower_bound);
        iterator.for_each(move |c| self.push(c));
    }

    #[inline]
    fn extend_one(&mut self, c: char) {
        self.push(c);
    }

    #[inline]
    fn extend_reserve(&mut self, additional: usize) {
        self.reserve(additional);
    }
}
```

Extend is here: https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#318-354
