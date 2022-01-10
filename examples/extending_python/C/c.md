https://realpython.com/cpython-source-code-guide/:
```
Python code is not compiled into machine-code. It is compiled into a special low-level intermediary language called bytecode that only CPython understands. This code is stored in .pyc files in a hidden directory and cached for execution. If you run the same Python application twice without changing the source code, it’ll always be much faster the second time. This is because it loads the compiled bytecode and executes it directly.
```

Still faster then running the same app twice would be to have Python call functions that are compiled to machine code. You can use C, C++ or Rust to extend Python. This is about extending Python with C. Extending Python with Rust is described [here](http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-='[ython-using-pyo3/).


### Data types

`int`: variable that can be used to contain integral values only
`float`: numbers that contain decimal places
`double`: same as float but with roughly twice the precision. Used when the range of a float is not sufficient.

### Compiling

```
gcc 01.c
gcc -o 01.exe 01.c
```


For a shared lib with Python (programm is named `add.c`):
```
gcc -c -fpic add.c
gcc -shared -o libadd1.so add.o
```
### memory

`malloc`: allocate some memory

```c
b = (char *)malloc(size);
```

C does not include a garbage collector. You have to free the memory yourself using `free`:

```c
free(b);
```