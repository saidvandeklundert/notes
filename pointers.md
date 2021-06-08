## Pointers in Python

In a Python program, it is not possible to use pointers directly.

Immutable: cannot be changed
- int
- float
- bool
- complex
- typle
- frozenset
- str

Mutable: can be changed
- list
- set
- dict

Even though pointers do not exists, mutable types can (sort of) be used as pointers.

In C:
```c
#include <stdio.h>

int main(void) {
    int y = 2337;
    printf("y = %d\n", y);
    add_one(&y);
    printf("y = %d\n", y);
    return 0;
}
```

In Python:
```python
>>> def add_one(x):
...     x[0] += 1
...
>>> y = [2337]
>>> add_one(y)
>>> y[0]
2338
```

Another example with Dictionaries:
```python
>>> counters = {"func_calls": 0}
>>> def bar():
...     counters["func_calls"] += 1
...
>>> def foo():
...     counters["func_calls"] += 1
...     bar()
...
>>> foo()
>>> counters["func_calls"]
2
```

Working with custom class and attributes is easier on the eye:
```python
class Metrics(object):
    def __init__(self):
        self._metrics = {
            "counter": 0,
        }

    @property
    def counter(self):
        return self._metrics["counter"]

    def inc_counter(self):
        self._metrics["counter"] += 1
        
```
Running it:
```
metrics = Metrics()
metrics.inc_counter()
metrics.inc_counter()
metrics.counter
```

## id() and is

`id()`: returns the memory address of an object.

`is`: returns True if 2 objects have the same memory address.



Pedantic, but Python does not have variables, rather it has names.

Example:
```python
x = 2337
```

This will 
1. Create a PyObject
2. Set the typecode to integer for the PyObject
3. Set the value to 2337 for the PyObject
4. Create a name called x
5. Point x to the new PyObject
6. Increase the refcount of the PyObject by 1

Note: The PyObject is not the same as Python’s object. It’s specific to CPython and represents the base structure for all Python objects.

PyObject is defined as a C struct, so if you’re wondering why you can’t call typecode or refcount directly, its because you don’t have access to the structures directly. Method calls like sys.getrefcount() can help get some internals.


If the refcount of a PyObject is 0, the garbage collector can clean it up.






List of sources used:
- https://realpython.com/pointers-in-python/#why-doesnt-python-have-pointers
