

https://github.com/rust-lang/rust/blob/master/library/std/src/collections/hash/map.rs


```rust
#[stable(feature = "rust1", since = "1.0.0")]
pub struct Keys<'a, K: 'a, V: 'a> {
    inner: Iter<'a, K, V>,
}

#[stable(feature = "rust1", since = "1.0.0")]
pub struct Values<'a, K: 'a, V: 'a> {
    inner: Iter<'a, K, V>,
}
```


To iterate a hashmap, use `keys()`, `values()` or `iter()`. To iterate and change the hasmap, use `values_mut()` or `iter_mut()`.