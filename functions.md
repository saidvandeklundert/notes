# Functions

Functions serve the following development roles:
- maximize code reuse, thereby minimizing redundancy.
- aide with procedural decomposition ( divide task into smaller chunks)

When a function is called, the caller stops untill the function is finished and returns control to the caller.

Variables assigned outside functions are global variables. Variables in a function are local variables. When the function returns, the local scope variables are destroyed/forgotten.

**LEGB** rule: Local, Enclosing functions, Global and Built-in. Exceptions are comprehension variables and variables local to an exception clause.

When functions are passed mutable objects (lists and dicts for instance), in place operations live on after the function is completed:

```python
x = 'string'
y = [ 1, 2, 3]

def change(a, b):
    a = 'yolo'
    b[2] = 'three'
    b = a

>>> change(x, y)
>>> x
'string'
>>> y
[1, 2, 'three']
```

To ensure you will not make any changes to a mutable object, you can:
- call a function like so: `change(x, y[:])`
- use copy/deepcopy inside the function (or outside and then pass the copy)
- pass a tuple to the function (less flexible)


In case a function does not have a return, Python automatically adds `return None`. When you add the return statement to a function without a value, then `None` is returned.

Function tips:
- keep functions small
- functions should have a single purpose
- use global variables only when you REALLY have to
- do not change mutable arguments
  - if you change mutable arguments, make it very explicit
- use arguments for input ad return for output

```python
# define function
def hello():
    return 'hello'

# call the function
hello()

# Access global values from a function:
x = 1
def function():
    global x    
    x = 2
>>> x
2    


# Functions can be passed as a parameter:
def example():
    print('yolo')

def another_example(f):
    f()

>>> another_example(example)     
yolo

# defaults:
def func(b=0):
    return b

>>> print(func())
0
>>> print(func(b=9)) 
9

# args and kwargs:
def args_and_kwargs(*args, **kwargs):
    """*args and **kwargs is just a naming convention"""
    print(args)
    print(kwargs)

>>> print(args_and_kwargs(1, 2, 'b', yolo=5, x = [ 1, 2,])) 
(1, 2, 'b')
{'yolo': 5, 'x': [1, 2]}

# Lambda/anonymous function example;
#  useful when you need a function but where it would be syntactically illegal.

def func(x):
    x = x * 2
    return (lambda x: x + 1 if x < 100 else 1)(x)
# Jumptable:
jt = [
    lambda x: x + 2,
    lambda x: x + 3,
    lambda x: x + 4
    ]
jt[0](3)

numbers = [ 1, 3, 10, 130]
list(filter(lambda x: x <= 10, numbers))
>>> [1, 3, 10]
```