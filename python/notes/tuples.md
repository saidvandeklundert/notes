# Tuples

Tuples are immutable ordered sequences. Tuples contain arbitrary objects that are accessed by index. Tuples are positionally ordered from left to right and can contain any kind of object (also mutable objects). The tuple itself stores a reference, not the actual object. 

Tuples can be sliced.

A reason for choosing tuples could be their immutability. This will provide an inintegrity constraing that could be convenient.

```python
# Empty tuple
()

# One item tuple:
x = (0,)

# Example of 2 tuples
x = (0, [ 1, 2,], 'sad', 1.9)
y = 0, [ 1, 2,], 'sad', 1.9

# Example of named tuple:
from collections import namedtuple
Router = namedtuple('router', ['name', 'role', 'ipv4', 'os']) 
spine01 = Router('spine01', 'spine', '192.168.1.1', 'eos')

# Object can be accessed by index and by name:
>>> [ x for x in spine01]
['spine01', 'spine', '192.168.1.1', 'eos']
>>> spine01.os
'eos'
>>> spine01.ipv4
'192.168.1.1'

# iterate tuple:
t = tuple('tuple')
for i in t: print(i)

# Repeat tuple
t * 3
>>> ('t', 'u', 'p', 'l', 'e', 't', 'u', 'p', 'l', 'e', 't', 'u', 'p', 'l', 'e')
# Concatenate tuple:
t + t
>>> ('t', 'u', 'p', 'l', 'e', 't', 'u', 'p', 'l', 'e')

# several sequence operations:
len(t)
start = 1; stop = 3 ; step = 1 
t[start:stop:step]
>>> ('u', 'p')
sorted(t) # returns a list
t.count('u')
```