### Mutability

| Object type        | Mutable |
| ------------------ |:-------------:|
| int                | no            |
| float              | no            |
| string             | no            |
| tuple              | no            |
| frozenset          | no            |
| list               | yes           |
| dictionary         | yes           |
| set                | yes           |
| bytearray          | yes           |



## Demonstrating immutability

Since the integer is immutable, we cannot truly change an integer. The following demonstrates that, instead of changing the value of the integer, we change the value that the variable is referencing to:
```python
>>> x = 0
>>> id(x) 
2282558810384
>>> x +=1
>>> id(x) 
2282558810416
>>>  
```

After changing the value of x from `0` to `1`, we are no longer pointing to the same memory address.

The list type is mutable, so we will be able to change the value of a list and keep working with the exact same object located at the exact same place in memory:
```python
>>> l = [0,1,2,3]
>>> id(l)
2282564914624
>>> l.append(4)
>>> del l[0]
>>> id(l)       
2282564914624
>>> 
```


## variables in Python

Technically, Python has `names` and it does not have `variables`.

Example:

```python
x = 0
```

In the previous, when you create `x`, the following happens:
1. a PyObject is created in memory
2. the PyObject has it's field set accordingly:
  - type is set to integer
  - value is set to `0`
3. a <b>NAME</b> is created, `x`
4. `x` is set to point to the PyObject and the reference count to that object is set to 1

![Python name](/img/python_variable_is_a_name.png "Python name")

A PyObject is the C implementation of the Python object, implemented in a struct. Every Python object is represented as a PyObject in memory.

If we change an immutable type, Python actually creates a new PyObject for us:

![Python change variable name](/img/python_change_var_name.png "Python change variable name")

The previous value now has the reference count set to 0 and it can be cleaned up by the garbage collector.

When we change a mutable type, like a list for instance, Python does not need to create a new PyObject. Instead, it can just update the value of the fields in the PyObject.


## Pass by value vs pass by reference (vs pass by assignment??)

Pass by value:
- value is copied to receiving function
- object will be duplicated in memory

Pass by reference:
- the receiving function is passed a pointer to a value
- the pointer is (oftentimes) much smaller then the value
- receiving functions can dereference that memory addres to work with the value directly

The above are the behaviors you can choose from in other languages like C or Go.

Python does it differently though, Python uses `pass-by-assignment`:
- the address of the PyObject is passed to the receiving function


So instead of passing in the data to a function, the address of the PyObject that contains the data is passed to the receiving function. 

This makes the behavior differ depending on the type of object passed into a function. When an `immutable` object is passed into a function, the behavior is similar to pass by value because the PyObject cannot be modified directly.

When a `mutable` object is passed into a function, the behavior is similar to pass-by-reference. This is because you can directly modify the PyObject being passed into the function without duplication.


Simple demonstration:
```python
>>> x = 0
>>> def add(x):
...     x += 1
...     print(f"x inside the func {x}")
... 
>>> add(x)
x inside the func 1
>>> x
0
>>>
### ^ Pass by value, x remains the same outside of the function
>>> l = [0,1,2]
>>> def remove(l):
...     del l[0]
...     print(f"l inside the function {l}") 
... 
>>> remove(l)
l inside the function [1, 2]
>>> l
[1, 2]
## pass by reference, the list is altered even outside the function

# beware that instantiating a new list using the name to a list inside the func
#  leads to working with an entirely new PyObject:
>>> l = [0, 1]
>>> add(l)
[0, 1, 2, 3]
>>> l
[0, 1]
```