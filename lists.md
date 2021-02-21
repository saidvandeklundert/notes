# Lists

Lists are mutable, ordered sequences that can contain any object. The list value refers to the list itself, not the values inside the list.


```python
# creating an empty list
x = []

# Lists can contain any object
x = [ 's', 1, 1.23, { 'a' : 'b' }, [], { 'a', 'b', 'c'}, tuple('aa',)]

# we can slice lists:
start = 1; stop = 3 ; step = 1 
x[start:stop:step]
>>> [1, 1.23]

# Get the last item of a list:
x[-1]
# Second to last:
x[-2]

# Get the lenght of the list:
len(x)

# Use list to build a list out of iterables:
list('yolo')


# Adding and removing items from a list:
x = []
# Add 1 item:
x.append(2)
# Extend the list with a list:
x.extend([3, 4, 5])
# insert an item (EX. 1) into the list (example position 0):
x.insert(0,1)

>>> x
[1, 2, 3, 4, 5]

# remove item (ex. 2) from list
x.remove(2)

# pop index 1 from list (returns and removes from list)x
>>> x
[1, 3, 4, 5]
>>> x.pop(1)
3
>>> x
[1, 4, 5]

# Delete item at index/ delete a slice:
del x[0]
del x[1:3]

# concatenate list (return is a new list):
x + x
# repeat list (return is a new list):
x * 3

#iterate the list
for i in x: print(i)

# test membership:
1 in x
>>> True

# Get index value of item (value error if item is not in list):
x.index(1)

# Count occurences of item in list:
x.count(1)

# sort items in a list in place 
# Notes: there is no return / Python cannot compare numbers and strings
x = ['a', 'Z', 'A', 'b', 'c',]
x.sort() # > ['A', 'Z', 'a', 'b', 'c'] ASCIIbetial order
x.sort(key=str.lower) # > ['A', 'a', 'b', 'c', 'Z'] regular alphabetical order
x.sort(key=str.lower, reverse=True) # > ['Z', 'c', 'b', 'A', 'a']

# reverse items in a list:
x.reverse()

# copy the list
x.copy()

# clear references in the list/empty the list
x.clear()
```