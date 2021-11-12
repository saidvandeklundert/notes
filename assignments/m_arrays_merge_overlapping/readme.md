Take in a non-empty array and merge overlapping intervals.


```
{
  "intervals": [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
  ]
}
```

The above should become the following:
```
[[1,2], [3,8],[9,10]]
```


Can be done in O(nlog(n)) time and O(n) space