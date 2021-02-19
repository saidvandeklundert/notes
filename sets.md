# Sets

Sets are a built-in type in Python. Sets have the following characteristics:
- set elements are unique
- set elements are unordered
- elements contained within a set must be of an immutable type
- the set itself can be altered even though it contains immutable objects only

Sets can be created using curly braces as well as through the use of the `set(<iter>)` function:

```python
set_example = set(['a', 'b', 'c',])
set_example = { 'a', 'b', 'c', }
```

If the curly braces are used, iterable objects are placed into the set intact. When the `set()` function is used, this is not the case.

The `set()` function can be used to create an empty set. Curly braces with nothing in them are interpreted as a dictionary.



## Common set operations

```python
# Add single immutable object to a set
x.add('d')

# Add elements from a set to a set:
x.update(['a', 'b', 'c'])

# check the difference between sets:
x1 = { 'a', 'b', 'c'}
x2 = { 'b', 'c', 'd'}
x1.difference(x2)
>>> {'a'}
# shorthand:
x1 - x2
>>> {'a'}

# check the union of sets (any elements present in any of the sets)
x1 = { 'a', 'b', 'c'}
x2 = { 'b', 'c', 'd'}
x3 = { 'e', 'f', 'c'}
x1.union(x2, x3)
>>> {'a', 'e', 'b', 'f', 'c', 'd'}

# check the intersection of sets (elements present in all of the sets)
x1 = { 'a', 'b', 'c'}
x2 = { 'b', 'c', 'd'}
x3 = { 'e', 'f', 'c'}
x1.intersection(x2, x3)
>>> {'c'}
x1 & x2 & x3 & x4

# shorthand to get the union of sets:
x1 & x2 & x3

# Get the difference between sets.
# following returns elements present in x1 but not in any of the other sets:
x1 = { 'a', 'b', 'c'}
x2 = { 'b', 'c', 'd'}
x3 = { 'e', 'f', 'c'}
x1.difference(x2, x3)
>>> {'a'}

# Get the symmetric difference:
#  elements which are in either of the sets, but not in their intersection
x1 = { 'a', 'b', 'c'}
x2 = { 'b', 'c', 'd'}
x1.symmetric_difference(x2)
>>> {'a', 'd'}

# shorthand:
x1 ^ x2

# isdisjoint: False if two sets have any elements in common, True otherwise:
x1 = { 'a', 'b', 'c'}
x2 = { 'b', 'c', 'd'}
x1.isdisjoint(x2)
>>> False

# subset: True if all elements of set is present in other set, False otherwise:
x1 = { 'a', 'b', 'c'}
x2 = { 'b', 'c', 'd'}
x1.issubset(x2)
>>> False
x1 = { 'a', 'b', 'c'}
x2 = { 'a', 'b', 'c', 'd'}
x1.issubset(x2)
>>> True

# superset: inverse of subset. True if all elements of set is present in other set, False otherwise:
x1 = { 'a', 'b', 'c'}
x2 = { 'a', 'b', 'c', 'd'}
x1.issuperset(x2)
>>> False
x2.issuperset(x1) 
>>> True
# Use < to check for proper subset, meaning sets cannot be identical:
x1 = { 'a', 'b', 'c'}
x2 = { 'a', 'b', 'c', 'd'}
x1 < x2
>>> True

# For comparisons, sets are order neutral:
set('abc') == set('cba')      
>>> True

# Filter duplicates from list and have a list returned:
list(set([1, 2, 1, 3, 1]))

# set comprehension
{n +1 for n in [1, 2, 3, 4]}
>>> {2, 3, 4, 5}
```