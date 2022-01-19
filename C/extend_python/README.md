A good deal of Python, or at least [CPython](https://github.com/python/cpython), is written in C. It is not only the languages and the interpreter that are powered by C. You can also find a lot of modules in the Python standard library powered by C right [here](https://github.com/python/cpython/tree/main/Modules).

Many things have been written about how C is used in Python. Once that I really enjoyed is the `CPython internals` book, written by Anthony Shaw.

What I was missing though, was something that explained in simple terms how to extend Python using C. Additionally, I was also curious about the C language myself. So I picked up a copy of 'The C programming language' and set out to write some basic C extensions. After having played with calling Rust from Python, described [here](http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-='[ython-using-pyo3/), it seemed like a nice project for me to entertain myself while being in between jobs.


# Why extend Python with C?


C is a compiled language that is very fast and efficient. It gives you low-level control over the hardware and you can run C programs on almost anything. It is possible to use C modules, that are compiled to machine code, directly in your Python programs.
 
Another valid reason for extending Python with C could be to learn about C and better understand Python.


# How to extend Python with C?

There are multiple options available to call C code from Python. The options that come with CPython by default are the following:
- using ctypes: https://docs.python.org/3/library/ctypes.html#module-ctypes
- Python API: https://docs.python.org/3/c-api/intro.html

In addition to these 2 options there is also the 'cffi', or 'C Foreign Function Interface' for Python. This package needs to be installed before you can use it. It is still maintained and usable with Python 3.10. You can find more information on cffi here: https://cffi.readthedocs.io/en/latest/index.html.


In this article, I will give a small example on how to call a C function using ctypes and after that, I will move on to using the Python API.

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
gcc -shared -o clib.so square.c
```

This will output a file called `clib.so`. This file is something we can import into our Python script. Let's put a `square.py` script in the same directory:

```python
import ctypes

c_lib = ctypes.CDLL("./clib.so")

print(c_lib.square(2))
```

That is it!

What happes in the above is we import `ctypes` so that we can use `ctypes.CDLL` to load the shared object library we produced as a module in Python. In the example, that 'module' is stored in the `c_lib` variable. The C functions, or in our case function, can then be called like so: `c_lib.square()`.


# Python API

The Python API is usable from C and C++. It is a maintained feature of Python and it is documented [here](https://docs.python.org/3/c-api/index.html). In case you want to have your C extensions added to Python, it is worth noting that you have to following [PEP 7](https://www.python.org/dev/peps/pep-0007/). It might also be worth knowing this PEP exists as helps clarify the formatting and style of the existing C code.

# Python API example

There are a number of steps to follow before you can call a C function from Python using the Python API. 

In your C file you need to:
- include the proper header file (`Python.h`)
- write a function
- put the function in a PyObject
- handle stuff like 'receiving' and 'returing' values from the Python runtime inside the PyObject
- add the PyObject to an array inside 'PyMethodDef'
- build the 'PyModuleDef' struct
- define 'PyMODINIT_FUNC' so that the module can be initialized


After this, you can make things easy for yourself and put in place a `setup.py` file that compiles the source code and installs it as a module for you. If you do this, you do not have to worry about whereto you are compiling or where the file you need to import is.




Some things about the C-extension up front:
- the C extension will be 1 file called `c_extension.c`
- the Python setup file will be used to build the extension and install it as a module called `c_extension`
- the function that we will expose from C to Python will be called `multiplier`

Let's first focus on the necessary C code.
## Creating the C extension


Our C-extension will provide a function that will be called `multiplier`. The C code is the following:

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

int multiplier(int a, int b)
{
    return a * b;
}

static PyObject *c_multiplier(PyObject *self, PyObject *args)
{
    int a;
    int b;
    int ret;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }
    ret = multiplier(a, b);
    return Py_BuildValue("i", ret);
}

static PyMethodDef module_methods[] = {
    {"multiplier", c_multiplier, METH_VARARGS, "Multiply two numbers."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef c_extension =
    {
        PyModuleDef_HEAD_INIT,
        "c_extension", // the name of the module in Python
        "",            // The docstring in Python
        -1,            /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        module_methods};

PyMODINIT_FUNC PyInit_c_extension(void)
{
    return PyModule_Create(&c_extension);
}
```


There is a lot going on here, so let's break it apart.

### include the proper header file

At the top of the file, we include the proper header file:

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>
```


### The C function
### The PyObject

Here we handle stuff like 'receiving' and 'returing' values from the Python runtime inside the PyObject.

### Adding the PyObject to 'PyMethodDef'

Adding the PyObject to an array inside 'PyMethodDef'.

### Define the 'PyModuleDef' struct
### Define 'PyMODINIT_FUNC' so that the module can be initialized





## The setup script

```python
from distutils.core import setup, Extension

module = Extension("c_extension", sources=["c_extension.c"])

setup(
    name="c_extension",
    version="0.1",
    description="An example of C extension made callable to the Python API.",
    ext_modules=[module],
)
```
## Installing and calling the function

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


# Some FYIs

On Windows, you will find an 'include' directory where Python is installed. On my system for instance, it was `C:\Python39\include`. Pointing your IDE to this directory makes coding easier.

On a Linux system, you might need to install the `python-dev` package. 

# Links relevant to the article:


[c modules](https://github.com/python/cpython/tree/main/Modules)
[header files](https://github.com/python/cpython/tree/main/Include)
[api docs](https://docs.python.org/3/c-api/index.html)
[structures](https://docs.python.org/3/c-api/structures.html)
[PyArg_ParseTuple arguments](https://docs.python.org/3/c-api/arg.html)
[PEP 7](https://www.python.org/dev/peps/pep-0007/)