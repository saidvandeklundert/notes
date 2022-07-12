"""

Lists are mutable, ordered sequences that can contain any object. The list value refers to the list itself, not the values inside the list.

When compared to other languages, it is worth noting that the Python list is a dynamic array.

Index and slice assignments are in-place changes. This means the list is modified instead of generating a new list.

When a list is assigned to a variable, the reference to the list is assigned to that variable. 

Example showing this by looking at the memory address:
"""
x = [1, 2, 3]
y = x
id(x)
# 140150413486976
id(y)
# 140150413486976
id(x[0])
# 140150440708000
id(y[0])
# 140150440708000


# Example with values:
x = ["a", "b", "c"]  # define a list
y = x  # copy reference to list to y variable
y[1] = "abc"  # change item 1 in the list
y  # item one in the list changed:
# ['a', 'abc', 'c']
x  # item 1 in x has changed as well because it is the same list
# ['a', 'abc', 'c']

x is y  # comparing identity:
# True

# creating an empty list
x = []

# Lists can contain any object
x = [
    "s",
    1,
    1.23,
    {"a": "b"},
    [],
    {"a", "b", "c"},
    tuple(
        "aa",
    ),
]

# index assignment:
x[0] = "t"

# we can slice lists:
start = 1
stop = 3
step = 1
x[start:stop:step]
# [1, 1.23]

# we can assign slices:
x[start:stop] = ["a", "b"]

# Get the last item of a list:
x[-1]
# Second to last:
x[-2]

# Get the lenght of the list:
len(x)

# Use list to build a list out of iterables:
list("yolo")


# Adding and removing items from a list:
x = []
# Add 1 item:
x.append(2)
# Extend the list with a list:
x.extend([3, 4, 5])
# insert an item (EX. 1) into the list (example position 0):
x.insert(0, 1)

x
# [1, 2, 3, 4, 5]

# remove item (ex. 2) from list when you know the value but not the index:
x.remove(2)

# pop index 1 from list (returns and removes from list)x
x
# [1, 3, 4, 5]
x.pop(1)
# 3
x
# [1, 4, 5]

# Delete item at index/ delete a slice:
del x[0]
del x[1:3]

# concatenate list (return is a new list):
x + x
# repeat list (return is a new list):
x * 3

# iterate the list
for i in x:
    print(i)

# test membership:
1 in x
# True

# Get index value of item (value error if item is not in list):
x.index(1)

# Count occurences of item in list:
x.count(1)

# sort items in a list in place
# Notes: there is no return / Python cannot compare numbers and strings
x = [
    "a",
    "Z",
    "A",
    "b",
    "c",
]
x.sort()  # > ['A', 'Z', 'a', 'b', 'c'] ASCIIbetial order
x.sort(key=str.lower)  # > ['A', 'a', 'b', 'c', 'Z'] regular alphabetical order
x.sort(key=str.lower, reverse=True)  # > ['Z', 'c', 'b', 'A', 'a']

# reverse items in a list:
x.reverse()

# copy the list
x.copy()

# clear references in the list/empty the list
x.clear()

# assign reversed list to a new list:
y = list(reversed([1, 2]))

# Create a list with 1000 empty containers:
x = [None] * 1000

# List comprehension

# values = [ expression
#           for item in collection
#           if condition
#           ]


devices = [
    "S1",
    "S2",
    "R1",
    "R2",
]
routers = [device for device in devices if "R" in device]
routers
["R1", "R2"]


# Nested list comprehension
[x + y for x in [1, 2, 3] for y in [4, 5, 6]]

# use copy to make a duplicate of a mutable value like (list or dict):
import copy

x = [
    1,
    2,
]
y = copy.copy(x)  # x is y >> False, x == y >> True
z = x  # x is z >> True

# use deepcopy if list contains other lists:
x = [1, 2, [1, 2]]
y = copy.deepcopy(x)  # x is y >> False, x == y >> True

# Unpacking a list to pass items as arguments:
x = [1, 2, 3, 4]
print(*x)
# 1 2 3 4
# Note, only gives the keys for dicts. For dicts key/values use **.

# unpacking lists:
x, y = ["a", "b"]
_, y = ["a", "b"]  # using _ is a convention to indicate the var is not used

# print 2 lists together:
x1 = ["a", "b", "c", "d"]
x2 = [1, 2, 3, 4]
for x, y in zip(x1, x2):
    print(x, y)
# ...
# a p
# b q
# c r
# d s

# Convert something to a single list without looping:
x = [
    "a",
    "b",
    ["c", "d"],
    ["e", "f"],
    [],
]
import itertools

list(itertools.chain.from_iterable(x))
# >>> ['a', 'b', 'c', 'd', 'e', 'f']

# Combine two lists:
a = [1, 2, 3]
b = [4, 5, 6]
c = list(itertools.chain.from_iterable(zip(a, b)))
c
# >>> [1, 4, 2, 5, 3, 6]


## List and string slicing examples:


x = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

first_two = x[:2]  # [ 1, 2,]
four_to_last = x[3:]  # [ 4, 5, 6, 7, 7, 8, 9, 10 ]
two_to_five = x[1:5]  # [ 2, 3, 4, 5]
last_three = x[-3:]  # [ 8, 9, 10]
skip_first_and_last = x[1:-1]  # [ 2, 3, 4, 5, 6, 7, 7, 8, 9]
copy_of_complete_list = x[:]  # [ 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10 ]
list_in_reverse = x[::-1]  # [10, 9, 8, 7, 7, 6, 5, 4, 3, 2, 1]

# x[start:end:step] 			   # list slicing syntax


# List implementation in Python 3.10: https://github.com/python/cpython/blob/3.10/Objects/listobject.c

# Deepdive on the list implementation in Python: http://www.laurentluce.com/posts/python-list-implementation/
