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



![Python change variable name](/img/python_change_var_name.png "Python change variable name")
