

# Interesting folders:

/CPYTHON
    /include: header files. Include these in your IDE.
    /objects: object implementations. Here you will find the `int`, `str`, `list`, etc.
    /python: interpreer, bytecode compiler & more infra
    /parser: parser, lexer and parser generator
    /modules: stdlib extensions and 'main.c'
    /programs: contains the 'real' main

# Interesting locations for specific things:

Some interesting objects:
[Enum](https://github.com/python/cpython/blob/main/Objects/enumobject.c)
[List](https://github.com/python/cpython/blob/main/Objects/listobject.c)
[int](https://github.com/python/cpython/blob/main/Objects/longobject.c)

[builtins module](https://github.com/python/cpython/blob/main/Python/bltinmodule.c)


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
