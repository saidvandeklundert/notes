# Extending Python with C


https://realpython.com/cpython-source-code-guide/:
```
Python code is not compiled into machine-code. It is compiled into a special low-level intermediary language called bytecode that only CPython understands. This code is stored in .pyc files in a hidden directory and cached for execution. If you run the same Python application twice without changing the source code, it’ll always be much faster the second time. This is because it loads the compiled bytecode and executes it directly.
```

Still faster then running the same app twice would be to have Python call functions that are compiled to machine code. You can use C, C++ or Rust to extend Python. This is about extending Python with C. Extending Python with Rust is described [here](http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-='[ython-using-pyo3/).

Options to extend/speed up Python with C:
- using ctypes: https://docs.python.org/3/library/ctypes.html#module-ctypes
- cffi library: https://cffi.readthedocs.io/en/latest/index.html
- Python API: https://docs.python.org/3/c-api/intro.html



# Using ctypes


When we use `ctypes`, we can write some C, compile it and then import the compiled C into our Python.

## A small example

An example would be the following C file called `square.c`:

```c
int square(int i)
{
    return i * i;
}
```

We can compile this file as follows:
```
gcc -shared -o clib.so square.c
```


This gives us a `clib.so` file that we can import into our Python script that could be as straightforward as the following code:

```python
import ctypes

c_lib = ctypes.CDLL("./clib.so")
x = c_lib.square(40)
print(x)
```


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