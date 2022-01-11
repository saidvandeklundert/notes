
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

# C coding standards PEP:

[PEP 7](https://www.python.org/dev/peps/pep-0007/)