# Functions

Functions serve the following development roles:
- maximize code reuse, thereby minimizing redundancy.
- aide with procedural decomposition ( divide task into smaller chunks)

When a function is called, the caller stops untill the function is finished and returns control to the caller.

Variables assigned outside functions are global variables. Variables in a function are local variables. When the function returns, the local scope variables are destroyed/forgotten.

When functions are passed mutable objects (lists and dicts for instance), in place operations may live on after the function is completed.


```python
# define function
def hello():
    return 'hello'

# call the function
hello()
```