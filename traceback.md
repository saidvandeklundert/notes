A traceback contains function calles made at a specific point. 

Tracebacks are also known under other names, such as `stack traceback`, `stack trace` and `backtrace` just to name a few.

Example script:

```python
def add(int1, int2):
    return int1 + int2

add("1", 2)
```

The above will produce the following:


```python
Traceback (most recent call last):
  File "example.py", line 5, in <module>
    add("1", 2)
  
  File "example.py", line 2, in add
    return int1 + int2

TypeError: can only concatenate str (not "int") to str  
```

Tracebacks are read bottom up. 

The final line in the traceback is the error message line. It tells you the type of exception that was raised and after this, the error message is displayed. In the above example, we see that we encountered a `TypeError` and the messages is `can only concatenate str (not "int") to str`.

Before the final line, we can see the vairous function calls that lead up to the exception. When reading from bottom to top, the function calls are listed from most recent to least recent.

Every function call has a two line entry:
- a first line containing the filename, linenumber and module name
- a second line conaining a reference to the code that was executed

Example:

```python
  File "example.py", line 2, in add
    return int1 + int2
```

Python has a built-in module called [traceback](https://docs.python.org/3/library/traceback.html). This can help you get more out of the traceback.