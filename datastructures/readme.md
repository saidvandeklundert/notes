
## Collections / linear datastructures:

- linked list
    - regular               d
    - doubly linked list
    - circular
- queue
- deque
- list
- stack                     d
- hash table
    - regular               d
    - with ll
    - with other algo
- array


## Non-linear datastructures:
- graph
- tree
    - regular tree
    - bin tree


## Algorithm analysis

We observe the space and the time that is required to execute and algorithm. To describe the differences of the algorithm, we turn to the 'Big-O notation'. This offers a means to describe the difference between solutions irrespective of the programming languagethat is in use or the hardware the algorithm is run on.

The 'dominant term' is used to describe the Big-O notation. This means that portion of the function that overpowers the rest is really all that matters.

| f(n)    |     name     |
|-------- |:------------:|
| 1       | constant     |
| log n   | logarithmic  |
| n       | linear       |
| n log n | log linear   |
| n2      | quadriatic   |
| n3      | cubic        |
| 2n      | exponential  |

Example:
```python
a = 2
b = 4
c = 9

# 3n2: this is the dominant part.
# 3 statements performed n2 times
# due to nested iteration
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
# 2n: two statements iterated n times:
for k in range(n):
    w = a * k + 45
    v = b * b
d = 33
```