Take in an array that represents a stack and recursively sort the stack in place.

Treat the array as a stack where the end of the array is the top of the stack.

You can only:
- pop elements from the top using `.pop()`
- push elements to the top using `.append()`
- peek at the top element by accessing the last element in the array

You cannot do other list/array operations and the solution must be recursive.


Example input:

```
[ -5, 2, -2, 4, 3, 1]
```

Output:
```
[ -5, -2, 1, 2, 3, 4]
```

It can be done in O(^2) time and O(n) space.