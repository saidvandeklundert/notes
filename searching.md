## Searching in Python.


## Binary search:


```python
def binarySearch(array, target):
    return binHelper(array, target, 0, len(array) - 1)


def binHelper(array, target, left, right):
    if left > right:
        return -1

    m = (left + right) // 2
    mv = array[m]

    if target == mv:
        return m
    elif target > mv:
        return binHelper(array, target, m + 1, right)
    else:
        return binHelper(array, target, left, m - 1)
```

Binary search is also implemented for you in Python. In the source, they have a pure Python implementation, but overwrite that func if the C extension is available.

Examples on using the built-in:

```python
def py_bisect_left(array, target):
    import bisect

    # bisec_left: start search at left-side of the array
    # bisec_right or bisect: start search at right-side of the array
    # both return the index where something should be inserted
    # when using bisect/bisect_right, deduct 1 from the returned index when
    # checking to see if that is the actual value
    idx = bisect.bisect_left(array, target)

    if idx < len(array) and array[idx] == target:
        return idx
    else:
        return -1


def py_bisect_right(array, target):
    import bisect

    idx = bisect.bisect_right(array, target)

    if idx <= len(array) and array[idx - 1] == target:
        return idx - 1
    else:
        return -1
```


To verify if an element exists in a collection, you can do either of the following:

```python
from search.binary import contains
array = [0,1,2]
contains(array, 1)
# or
1 in array
```
## Linear search

Traverse all elements in the array:
```python
def linear(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1
```

Note,

Python already implements linear search as part of the standard library. This implementation is written in C and WILL be faster then your version of it in Python.

The list data structure has the following methods:

```python
>>> [0, 1, 21, 355].index(355) 
3
```

