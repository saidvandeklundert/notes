Take in a non-empty array of distinct integers and a target sum.

Find out all quadruplets that can summ up to target sum and return a two-dimensional array of all those quadruplets in no particular order.

If nothing can make the sum, return an empty array.

Average is O(n^2) time and O(n^2) space where n is th length of the input array.

Worst is O(n^3) time and O(n^2) space.

Example input:

```
[ 7, 6, 4, -1, 1, 2]
```
Target 16

Example output:

```
[[7, 6, 4, -1], [7, 6, 1, 2]]
```

