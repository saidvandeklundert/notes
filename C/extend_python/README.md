https://realpython.com/cpython-source-code-guide/:
```
Python code is not compiled into machine-code. It is compiled into a special low-level intermediary language called bytecode that only CPython understands. This code is stored in .pyc files in a hidden directory and cached for execution. If you run the same Python application twice without changing the source code, it’ll always be much faster the second time. This is because it loads the compiled bytecode and executes it directly.
```

Still faster then running the same app twice would be to have Python call functions that are compiled to machine code. You can use C, C++ or Rust to extend Python. This is about extending Python with C. Extending Python with Rust is described [here](http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-='[ython-using-pyo3/).

Options to extend/speed up Python with C:
- using ctypes: https://docs.python.org/3/library/ctypes.html#module-ctypes
- cffi library: https://cffi.readthedocs.io/en/latest/index.html
- Python API



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


### Python API


At the top of the file, you need to pull in the Python API:

```python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
```

On Windows, you will find an 'include' directory where Python is installed. On my system for instance, it was `C:\Python39\include`. On a Linux system, you might need to install the `python-dev` package.
