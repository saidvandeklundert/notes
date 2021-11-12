The array that is given represents a number of jumps.

If the item is 2, then you need to jump 2 indexes forward.

If it is -3, you need to jum backward 3 indexes.

The array wraps around. If you are at 0 and you jump -1, you will be at the end of the array.

THe function should check if, when you do all the jumps in the array, you have isisted every item before landing back on the starting index.

Example:
```
[2, 3, 1, -4, -4, 2]
```

True


It can be done in O(n) time and O(1) space.