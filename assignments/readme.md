
## Steps to using FFI:


1. create a new Cargo library project
2. modify the `Cargo.toml` and specify we are building a dynamic Rust library using `#[crate_type = "dylib"]` (example is [here](https://github.com/saidvandeklundert/python/blob/main/rust/pyru/Cargo.toml))
3. write a FFI in Rust that is compatible with C
4. build the library using the regular `cargo build --release`
5. Create a Python program that loads the library and calls the function. On Linux, load the `.so` file.

An example library made by me is [pyru](https://github.com/saidvandeklundert/python/tree/main/rust/pyru).


## Using py03:



```
apt-get install python3-venv
python3  -m venv .env
source .env/bin/activate
pip install maturin
cd rust_lib/
maturin develop
export PS1='# '
(.env) root@rust:/var/tmp/rust_from_python/string_sum# python3 
Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import string_sum
>>> string_sum.sum_as_string(5, 20)
'25'
```