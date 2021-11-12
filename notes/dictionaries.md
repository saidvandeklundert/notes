Dictionaries are mutable mappings. 

Inside a dicitonary, items are stored and fetched by key.

Dictionary keys can be any immutable type. The values can be immutable as well as mutable objects.

They is 1 value per key, but there may be many keys per value.

As of Python 3.7, the dictionary maintains the order of the items of the dictionary.

Common ditionary operations:

```python
# Defining a dictionary:
d = {}
d = {'a' : [1, 2, ]}

# Dictionary construction examples:
d = dict(name='said', age=35) 
d = dict([('name', 'said'), ('age', 35)]) 
d = dict(zip(keyslist, valueslist)) 
d = dict.fromkeys(['name', 'age'])          # {'name': None, 'age': None}

# Check if key exists in Dict:
"age" in d          # this tests against the keys
"age" in d.keys()
"age" in d.values()

# Common dictionary methods:

# Get a list of all keys:
d.keys()    

# Get a list of all the values:
d.values()

# Get all the keys and values:
d.items()

# Make a top-level copy:
d.copy()

# Remove all items:
d.clear()

# Merge dictionaries by keys:
d.update(d_2)

# Another way to merge dictionaries:
x = {'a': 1, 'd': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}

# Get key:
d.get('keyvalue', None)

# Return and remove key:
d.pop('said')

# Return and remove list item from a dictionary:
d.popitem()

# Check number of stored entries:
len(d)

# Delete key:
del d['key']

# Add or change key:
d['key'] = 23

# Set a default value:
d.setdefault("description", "unused")

# Dict comprehension:
d = { x: '_' for x in range(10) }

# Handle key error:
try:
    print(d['key'])       
except KeyError:            
    print('key-error')                    

# Make a tuple of tuples out of a dictionary:
tuples = list(d.items())

# Find interesting values using list comp:
[key for (key, value) in d.items() if value > 300]

# Print kv of a dict:
for k,v in d.items():
    print(k,v)
# Get items as tuple:
for tup in d.items():
    print(type(tup))
    print(tup)
# iterate dictionary sorted on key:
for key in sorted(d):
    print(f"{key} {d[key]}")
```