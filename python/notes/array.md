The array module is a thin wrapper on C arrays. It can hold only homogeneous data but it is more efficient then a list or tuple. Lists in Python use a lot more space than C arrays, in part because each item in the list requires the construction of an individual Python object.

In an array, the elements are more tightly packed. Tradeoff is that you can only store elements of the same type.





```python
>>> arr
array('b', [1, 3, 80, 30])
>>> x
[1, 3, 80, 30]
>>> sys.getsizeof(arr) 
68
>>> sys.getsizeof(x)   
120
```

You can store the basic C types in an array. Check the docs to figure out what code to use for a type: https://docs.python.org/3/library/array.html.


Arrays support many of the same methods as regular lists. 

```python
>>> import array
>>> arr = array.array('b', (1, 2, 3, 4))
>>> arr[1]
2
>>> arr
array('b', [1, 2, 3, 4])

# change
>>> arr[3] = 80 
>>> arr    
array('b', [1, 2, 3, 80])

# del
>>> del arr[1]
>>> arr        
array('b', [1, 3, 80])

# append
>>> del arr[1]
>>> arr        
array('b', [1, 3, 80])

# array is typed:
>>> arr[1] = "string"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: an integer is required (got type str)
>>> arr[1] = 4000    
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: signed char is greater than maximum
```
