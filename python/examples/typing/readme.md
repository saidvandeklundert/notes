
Python is `dynamically typed` and `strongly typed`:
- dynamically typed: after declaring a variable of a certain type, you can later on
 reassign that variable to be of another type.

```python
a = 1
a = "1"
```
- strongly typed: Python will not automatically convert a type into something else
 in order to make things work. Example:
 
```python
>>> ["example"] + "asa"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list
```

## Pros:

Improve the readability of the code

Communicate the semantics of the code to other and future developers

Get assistence from the IDE while coding

Have static code analysis tools point out errors before runtime!!

## Cons:

Higher entry barrier for people to start adding to the code base

Can sometimes be difficult or frustrating to explain to someone:
 why something is wrong due to a typing issue even though the 
 program is correct

Using complext type definitions (like generics) can produce complicated errors

Functionality can sometimes be restricted:
 handling int and floats oftentimes works, but type hints might restrict that
