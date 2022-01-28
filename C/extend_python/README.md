A good deal of Python, or at least [CPython](https://github.com/python/cpython), is written in C. The language and the interpreter are implemented in C and in addition to this, you can also find a lot of modules in the Python standard library powered by C.

Many things have been written about how C is used in Python. One that I really enjoyed is the `CPython internals` book, written by Anthony Shaw.

What I was missing though, was something that explained in detailed and simple terms how to extend Python using C. Additionally, I was also curious about the C language myself. So I picked up a copy of 'The C programming language' and set out to write some basic C extensions. After having played with calling Rust from Python, described [here](http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-='[ython-using-pyo3/), it seemed like a nice project for me to entertain myself while being in between jobs. What I wanted to get out of this was to understand a bit more about Python and to be able to read and browse the Python source code. 

In this article, I will extend Python with a C function using `ctypes` and the `Python C API`. After this, I will go over some (in my opinion) interesting places to browse in the CPython repository. I will wrap up with some interesting links to resources that can possibly help you further along in case you want to move past the toy examples and start using it more seriously.

# Why extend Python with C?


C is a compiled language that is very fast and efficient. In some cases, the speed of a program can be increased 10x to 100x. Additionally, using a C extension module can unlock some of the other advantages that C brings. To name 2:
- C gives you low-level control over the hardware 
- there are a log of other C modules that you will be able to leverage directly in your code
 
For me personally, the only reason I have is getting more familiar with C and CPython. If I _really_ had to extend Python to speed things up, I would probably turn to Rust.


# How to extend Python with C?

There are multiple options available to call C code from Python. The options that come with CPython by default are the following:
- `ctypes`: https://docs.python.org/3/library/ctypes.html#module-ctypes
- `Python API`: https://docs.python.org/3/c-api/intro.html

In addition to these 2 options there is also the 'cffi', or 'C Foreign Function Interface' for Python. This package needs to be installed before you can use it. It is still maintained and usable with Python 3.10. You can find more information on cffi here: https://cffi.readthedocs.io/en/latest/index.html.


In this article, I will give a short example on how to call a C function using ctypes. After that, I will move on to using the Python API and do a detailed walkthrough. In closing, I will list some interested docs and things to checkout as next steps.

The ctypes part I did on Ubuntu (20.04.3 LTS) using Python 3.10. I did not have to install anything other that Python in order to get this to work. 

The Python API part was done on Ubuntu as well. In order to get that to work, I had to pip-install `python-dev`. On Windows, I had to install Python 3.10 and Visual Studio Build tools 2019. Much to my amazement, it worked without any issues!

#  Extending Pythong with C using ctypes


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



# Extending Pythong with C using the Python API

The Python API is usable from C and C++. It is a maintained feature of Python and it is documented [here](https://docs.python.org/3/c-api/index.html). In case you want to have your C extensions added to Python, it is worth noting that you have to following [PEP 7](https://www.python.org/dev/peps/pep-0007/). It might also be worth knowing this PEP exists as helps clarify the formatting and style of the existing C code.

Interestingly enough, CPython also leverages this very same API. It is not for the faint of heart, but if you want to, you can check out the source code for the builtins for instance right [here](https://github.com/python/cpython/blob/main/Python/bltinmodule.c). This is a whopping 3.000 lines of code at the time of writing. The next example I will walk through next is a little lighter. It does however follow a similar flow.

# Python API example


What we will end up having is a C extension module called `c_extension` with a function called `multiplier`. We will end up being able to do the following:

```python
PS C:\> python

>>> from c_extension import multiplier
>>> multiplier(2,2)
4
>>> multiplier(200,200)
40000
```



There are a number of steps to follow before you can call a C function from Python using the Python API. 

The high level steps I am taking in the C file are the following:
- write a function and put the function in a PyObject
- add the PyObject to an array inside 'PyMethodDef'
- build the 'PyModuleDef' struct
- define 'PyMODINIT_FUNC' so that the module can be initialized

There are also some smaller things that I will take into account. When I include those smaller things, the following becomes the 'todo' when creating the C extension:
- include the proper header file (`Python.h`)
- write a function
- put the function in a PyObject
- handle stuff like 'receiving' and 'returing' values from the Python runtime inside the PyObject
- add the PyObject to an array inside 'PyMethodDef'
- build the 'PyModuleDef' struct
- define 'PyMODINIT_FUNC' so that the module can be initialized


After running through these steps, you can make things easy for yourself and put in place a `setup.py` file that compiles the source code and installs it as a module for you. If you do this, you do not have to worry about whereto you are compiling or where the file you need to import is.


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

This header file contains C declarations and macros. Basically, this pulls in the C-API. In this case, the `python.h` header file contains a lot of declarations that are relevant for us to be able to use the Python API.

Directing the C preprocessor to include this header file is like pasting in the code itself.

This header file is located in the `include` directory where you have installed Python. A good idea would be to point your idea to also use header files from this location. This way, you can hover over the structs and functions etc. On the same note, another good idea for when you like to explore the CPython source code, is to clone the CPython repo and browse the code base using your IDE. This will make it easier to see how the whole code base is glued together.


### The C function

The following is the actual C function that we will be able to call from Python:

```c
int multiplier(int a, int b)
{
    return a * b;
}
```

Lame, I know. But the point here is me sharing how to extend Python.
### The PyObject

Next up is the PyObject. The PyObject is the base struct of which all other Python objects are an extension. Here we define what the function receives and returns from Python:

```c
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
```

The first three lines define the integers 'a', 'b' and 'ret'. The values of 'a' and 'b' will be passed to the `multiplier` function, and the `ret` value will hold the return value of the `multiplier` function.

After our declarations, we see a call to `PyArg_ParseTuple()`. This will parse the arguments received from Python (`args`). The `ii` specifies that we are expecting 2 integer values. The `&a` and `&b` are the pointers that will come to contain the parsed values. These are pointing to the variables we declared earlier.

In case you want to use values other then integer values in your C extension, you can check the [PyArg_ParseTuple arguments](https://docs.python.org/3/c-api/arg.html) to understand what arguments you need to pass.

After this, we run the function and return `ret` to Python. For this, we use `Py_BuildValue()`, which is the counterpart of `PyArg_ParseTuple`. Where `PyArg_ParseTuple` translates something from Python to C, `Py_BuildValue` does the opposite. In our case, we indicate that we will return the value in `ret` as an integer object.

### Adding the PyObject to 'PyMethodDef'

Next up is putting everything we want to expose to Python in the 'method table', or `PyMethodDef`:

```c
static PyMethodDef module_methods[] = {
    {"multiplier", c_multiplier, METH_VARARGS, "Multiply two numbers."},
    {NULL, NULL, 0, NULL}};

```

In the above example, `module_methods` is a static array containing `PyMethodDef` structures. Since we only want to expose 1 function, we only put in the following entry:

```c
{"multiplier", c_multiplier, METH_VARARGS, "Multiply two numbers."}
```

These values signify the following:
- multiplier: the name the function will have in Python
- c_multiplier: the PyObject we created that calls the C function
- METH_VARARGS: bitfield, indicating the calling convention
- "Multiply two numbers.": the docstring for the Python function

More information can be found [here](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef).

The other line, `{NULL, NULL, 0, NULL}`, is a sentinal value, indicating that the preceeding value was the last relevant item in the array.

### Define the 'PyModuleDef' struct

Now, we define the `PyModuleDef` struct, which will describe our Python C extension module:

```c
static struct PyModuleDef c_extension =
    {
        PyModuleDef_HEAD_INIT,
        "c_extension", // the name of the module in Python
        "",            // The docstring in Python
        -1,            /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        module_methods};
```

The [doc](https://docs.python.org/3/c-api/module.html) says to always initialize the first member of this struct to 'PyModuleDef_HEAD_INIT', so I did that (without being able to figure out why).

The other lines are annotated and the final field is a pointer to the method table we defined earlier. This was the array of `PyMethodDef`, which contains all the functions (or 1 function in our case) that we want to expose to Python.



### Define 'PyMODINIT_FUNC' so that the module can be initialized

Lastely, we define the `PyMODINIT_FUNC` function, which is called when Python imports the extension module. This function returns the module struct that we defined previously:

```c
PyMODINIT_FUNC PyInit_c_extension(void)
{
    return PyModule_Create(&c_extension);
}
```

Ensure that the `PyMODINIT_FUNC` is correctly named. The last part should be the same as the module name (in this case, `c_extension`). 
## Installing and calling the function

Creating a `setup.py` will make things easier as you will be able to 'pip install' it and make it available to your local instance of Python. I put in place the following:

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

After cloning the repo, all I had to do is the following:

```
pip install src/
```

This will compile the source file and install the C extension module. You will see the packages installed when you run `pip freeze`.

We can now run the test script and observe the following:

```
python .\test.py
100
```

Awesome!



# Some FYIs

On Windows, you will find an 'include' directory where Python is installed. On my system for instance, it was `C:\Python39\include`. Pointing your IDE to this directory makes coding easier as this is where the header files are.

Also, much to my own surprise, I did not run into any issues on Windows. I installed Visual Studio Build tools 2019 and everything just worked.


I also tried out the example repo on Ubuntu. The only thing I needed to install was the `python-dev` package. 

# Next steps

In case you are interested in creating more serious C extension for Python, I think the official Python documentation is quite good, you can find the documentation on the API [here](https://docs.python.org/3/c-api/index.html). Additionally, there is a good talk you could look at [Paul Ross - Here be Dragons PyCon 2016](https://www.youtube.com/watch?v=Yq__HtUIH5Y). This person has put up quite a few examples and patterns for others to learn from right [here](https://pythonextensionpatterns.readthedocs.io/en/latest/index.html).
# Closing thoughts.

This was a nice excercise. I read K&R and played with C. I (tried) reading parts of CPython and I investigated how to extend Python with some C code.

Few personal things I learned:
- C may be a small language, reading and working with C can be quite challenging
- the C Python source code is not for the faint of heart
- extending Python with Rust was a lot easier due to the ergonomics put in place by PyO3



# Links relevant to the article:


[c modules](https://github.com/python/cpython/tree/main/Modules)
[header files](https://github.com/python/cpython/tree/main/Include)
[api docs](https://docs.python.org/3/c-api/index.html)
[structures](https://docs.python.org/3/c-api/structures.html)
[Extending Python with new types tutorial](https://docs.python.org/3/extending/newtypes_tutorial.html)
[PyArg_ParseTuple arguments](https://docs.python.org/3/c-api/arg.html)
[PEP 7](https://www.python.org/dev/peps/pep-0007/)
[Paul Ross - Here be Dragons PyCon 2016](https://www.youtube.com/watch?v=Yq__HtUIH5Y)
[Paul Ross - A faster Python? You Have These Choices](https://www.youtube.com/watch?v=5js_-pLGqwA)
[Python Extension Patters](https://pythonextensionpatterns.readthedocs.io/en/latest/index.html)
[CPython internals](https://www.amazon.com/CPython-Internals-Guide-Python-Interpreter/dp/1775093344)
[PyCon 2009 - nedbatchelder](https://nedbatchelder.com/text/whirlext.html)