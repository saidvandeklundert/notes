A good deal of Python, or at least [CPython](https://github.com/python/cpython), is written in C. Many things have been written about how C is used in Python. Once that I really enjoyed is the `CPython internals` book, written by Anthony Shaw.

What I was missing though, was something that explained in simple terms how to extend Python using C. Additionally, I was also curious about the C language myself. So I picked up a copy of 'The C programming language' and set out to write some basic C extensions. It seemed like a nice project for me to entertain myself while being in between jobs.


In case you are interested in extending Python with Rust, that is described [here](http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-='[ython-using-pyo3/).



You can extend Python with your own C code. Python can call C functions that are compiled to machine code. 
# Why extend Python with C?

C is a compiled language that is very fast and efficient. It gives you low-level control over the hardware and you can run C programs on almost anything. 

Another valid reason could be to learn about C and better understand Python / certain parts of Linux.


# How to extend Python with C?

There are multiple options available to call C code from Python. The options are the following:
- using ctypes: https://docs.python.org/3/library/ctypes.html#module-ctypes
- cffi library: https://cffi.readthedocs.io/en/latest/index.html
- Python API: https://docs.python.org/3/c-api/intro.html

 First, I will give a small example on how to call a C function using ctypes. After this, I will move on to using the Python API.

# Using ctypes


When we use `ctypes`, we can write some C, compile it and then import the compiled C into our Python.

Let's look at an example function in a file called `square.c`:

```c
int square(int i)
{
    return i * i;
}
```

Before we can call this function from our Python code, we need to compile it. And when we compile the code, we also need to pass in a flag so that the produced file can be imported. So after we put in place the C file, run the following command:

```
gcc -shared -o `square.so` square.c
```

This will output a file called `square.so`. This file is something we can import into our Python script. Let's put a `square.py` script in the same directory:

```python
import ctypes

c_lib = ctypes.CDLL("./square.so")

print(c_lib.square(2))

for i in range(10):
    x = c_lib.square(i)
    print(x)
```

That is it!

We import `ctypes` so that we can use `ctypes.CDLL` to load the binary we produced as a module in Python. In the example, that 'module' is stored in the `c_lib` variable. The C functions, or in our case function, can then be called like so: `c_lib.square()`.


# Python API

The Python API is usable by C and C++. It is a maintained feature of Python and it is documented [here](https://docs.python.org/3/c-api/index.html). In case you want to have your C extensions added to Python, it is worth noting that you have to following [PEP 7](https://www.python.org/dev/peps/pep-0007/). It might also be worth knowing this PEP exists as it clarifies some of the existing C code.

## A small example

At the top of the file, you need to pull in the Python API:

```python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
```

On Windows, you will find an 'include' directory where Python is installed. On my system for instance, it was `C:\Python39\include`. On a Linux system, you might need to install the `python-dev` package.


# Using the example extensions


There are several example extensions in this folder. Here is an example on how to install and run the `functions` example:

```
root@pyo3:/var/tmp/python/C/extend_python/python_api# pip install -e functions/src/
```

Most extension modules have an `example.py` and a `test.py` file that you can run:

```
root@pyo3:/var/tmp/python/C/extend_python/python_api# python3 functions/src/example.py 
Hello from C
root@pyo3:/var/tmp/python/C/extend_python/python_api# python3 functions/src/test.py    
Hello from C
```



# making an extension module:

Let's say the package is located in the `src/` directory. If it has the `setup.py` file, then the following will build and install the package:

```
pip install -e src/
```

When you run `python setup.py build`, the package will be built into a 'build' subdir and python will not import this file 'automatically' when it starts. 
# C modules:

```
Source files for standard library extension modules,
and former extension modules that are now builtin modules.
```
[c modules](https://github.com/python/cpython/tree/main/Modules)

# C header files:


[header files](https://github.com/python/cpython/tree/main/Include)

# C-API:

[api docs](https://docs.python.org/3/c-api/index.html)

[structures](https://docs.python.org/3/c-api/structures.html)

[PyArg_ParseTuple arguments](https://docs.python.org/3/c-api/arg.html)
# C coding standards PEP:

[PEP 7](https://www.python.org/dev/peps/pep-0007/)