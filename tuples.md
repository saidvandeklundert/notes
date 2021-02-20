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
```