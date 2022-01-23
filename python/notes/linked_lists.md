Some well known-collection types in Python are the following:
- lists
- tuple
- sets
- dictionaries

The link-list is also a collection type, but it is not one provided as a standard data type in Python.


Linked lists are used in the construction of other data types also. The `stack` (LIFO) and the `queue` (FIFO) make use of the linked list. 

### List:

A list is a collection of elements stored contiguously.

In CPython, the list is represented as a C-array. When data is stored in a Python list, the thing that is actually stored is a pointer to a PyObject memory address that is used to store the data. These pointers themselves are not pointing to contigous memory addresses. This means that indirectly, a Python list is not completely contigous as actual data is located at random places in RAM.

The C-array cannot grow or shrink after it is created. WHen you insert something into a list, all items after the insertion point need to be moved. If the underlying C-array is out of space, a new array needs to be created and the existing array needs to be copied into it.


### Linked list

A linked list does not have a backing array in C under the hood. Linked lists can grow and shrink in size.

Every node in the linked list is stored in a random location. A linked list is made up of nodes that store 2 things:
- data
- location of the next node in the linked list

One of the nodes has a 'special' head pointer that signifies it is the start of the list, or rather, that it is the 'head' node.

The last node in a linked list will not point to a next node, it will point to `None`.

To traverse the linked list, you start at the head and follow the nodes. You cannot start in the middle of a linked list or retrieve a specific item from the list in an O(1) operation like you can in a regular list.

There are two types of variants to the 'normal' linked list:
- doubly linked list
- circularly linked list

In a `doubly linked list`, every node contains a reference to the previous node as well as a refernce to the next node. This is what the `collections` module offers through the `deque` data structure.

In a `circularly linked list`, the tail node points to the head node. Some example use cases:
- manage app life cycle
- have players take turns 

### Building datastructures using linked lists:


#### Stack using a linked list:

The stack is a data structure that follows LIFO. You can add something to the top of the stack and you can remove something from the top of the stack. Because you can only work with the top element, the linked list is a usefull data structure you can use to implement a stack.

#### queue using a linked list:

A queue is a data structure that follows FIFO. It is kind of like a real world queue of people waiting for something.

You can only insert items at the rear of the queue (enqueue) or remove items from the front of the queue.   (dequeue).

#### Graps using linked list

The graph is also oftentimes implemented using a linked list. A graph shows relationships between connected entities. An example could be a collection of nodes that depict a topology. 


### collections.deque

The `collections` module offers the `deque`, which stands for "double-ended-queue". This data structure offers insertion and removal at the end or start of the lined list in O(1) time.

The source for `deque` can be found in the [collections](https://github.com/python/cpython/tree/main/Lib/collections) module, which will eventually lead you to [_collectionsmodule.c](https://github.com/python/cpython/blob/main/Modules/_collectionsmodule.c) where the `deque` is implemented in C.

```python
>>> from collections import deque 
>>> llist = deque([1,2,3]) 
>>> llist
deque([1, 2, 3])
>>> llist.append(4)   
>>> llist
deque([1, 2, 3, 4])
>>> llist.pop()    
4
>>> llist       
deque([1, 2, 3])
>>> llist.appendleft(0)
>>> llist
deque([0, 1, 2, 3])
>>> llist.popleft() 
0
>>> llist
deque([1, 2, 3])
```

You can make a waiting line (queue) using the `deque`:

```python
>>> from collections import deque
>>> waiting_line = deque()
>>> waiting_line.append("Jan")
>>> waiting_line.append("Marie") 
>>> waiting_line.append("Ingrid") 
>>> waiting_line.append("Anne")   
>>> waiting_line.append("Said") 
>>> waiting_line.popleft()     
'Jan'
>>> waiting_line.popleft()
'Marie'
>>> waiting_line.popleft()
'Ingrid'
>>> waiting_line.popleft()
'Anne'
>>> waiting_line.popleft()
'Said'
```

Making a stack using `deque`:
```python
>>> #stack of books
>>> sob = deque()
>>> sob.appendleft("fluent python")
>>> sob.appendleft("atbswp")
>>> sob.appendleft("learning python")
>>> sob
deque(['learning python', 'atbswp', 'fluent python'])
>>> sob.popleft() 
'learning python'
>>> sob.popleft()
'atbswp'
>>> sob.popleft()
'fluent python'
```

## Linked list Big O notations:


[cheatsheet](https://www.bigocheatsheet.com/)

