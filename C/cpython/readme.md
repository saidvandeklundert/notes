# Interesting folders:

/CPYTHON
    /include: header files. Include these in your IDE.
    /objects: object implementations. Here you will find the `int`, `str`, `list`, etc.
    /python: interpreter, bytecode compiler & more infra
    /parser: parser, lexer and parser generator
    /modules: stdlib extensions and 'main.c'
    /programs: contains the 'real' main

# Interesting locations for specific things:

Interesting modules:
[builtins module](https://github.com/python/cpython/blob/main/Python/bltinmodule.c)

Here, all the builtin functions etc are defined. At the bottom, after the module definition, there is the definition of all the builtin names that you use in Python. Part of the code:
```c
#define SETBUILTIN(NAME, OBJECT) \

    SETBUILTIN("False",                 Py_False);
    SETBUILTIN("True",                  Py_True);
    SETBUILTIN("bool",                  &PyBool_Type);
    SETBUILTIN("bytearray",             &PyByteArray_Type);
    SETBUILTIN("bytes",                 &PyBytes_Type);
    SETBUILTIN("dict",                  &PyDict_Type);
    SETBUILTIN("enumerate",             &PyEnum_Type);
    SETBUILTIN("float",                 &PyFloat_Type);
    SETBUILTIN("int",                   &PyLong_Type);
    SETBUILTIN("list",                  &PyList_Type);   
    SETBUILTIN("set",                   &PySet_Type);
    SETBUILTIN("str",                   &PyUnicode_Type);
    SETBUILTIN("tuple",                 &PyTuple_Type);

    return mod;
```

You can check it out and then at least you know what to look for as it offers some nice clues as to what specific object a keyword is implemented with.

Some interesting objects:
- dict:
[Include/dictobject.h](https://github.com/python/cpython/blob/main/Include/dictobject.h)
[Include/cpython/dictobject.h](https://github.com/python/cpython/blob/main/Include/cpython/dictobject.h)
[Dictobject](https://github.com/python/cpython/blob/main/Objects/dictobject.c)
[pycore dict](https://github.com/python/cpython/blob/main/Include/internal/pycore_dict.h)

- enum:
[Enum](https://github.com/python/cpython/blob/main/Objects/enumobject.c)

- list:
[List](https://github.com/python/cpython/blob/main/Objects/listobject.c)
[Include/listobject.h](https://github.com/python/cpython/blob/main/Include/listobject.h)

- int:
[int](https://github.com/python/cpython/blob/main/Objects/longobject.c)

- float:
[PyFloatObject](https://github.com/python/cpython/blob/main/Include/floatobject.h)

- object:
[Generic PyObject](https://github.com/python/cpython/blob/main/Include/object.h)





# Finding the source code for something.

Display the module's `__file__`:
```python
>>> import os
>>> os.__file__
'C:\\Users\\vandeklundert\\AppData\\Local\\Programs\\Python\\Python310\\lib\\os.py'
```

When you use inspect, you can also check where a class or other type of object is located:
```python
>>> import inspect
>>> inspect.getfile(Path)
'C:\\Users\\vandeklundert\\AppData\\Local\\Programs\\Python\\Python310\\lib\\pathlib.py'
>>> inspect.getsource(Path)
    'class Path(PurePath):\n    """PurePath subclass that can make system calls.\n\n    Path represents a filesystem path but unlike PurePath, also offers\n    methods to do system calls on path objects. Depending on your system,\n
    ...
    # the rest of the source code for the Path class
  
>>>
```


https://stackoverflow.com/questions/8608587/finding-the-source-code-for-built-in-python-functions



[Exploring CPython](https://devguide.python.org/exploring/)