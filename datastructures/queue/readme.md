# Queue

A Queue is a linear data structure where items are typically stored first in first out. The item that is inserted first will be removed first, just like people waiting in line for something.

Common queue operations are:
- enqueue: add element to the end of the queue
- dequeue: remove an element from the queue 
- front: return the first element
- rear: return the last element

The time complexity for all of the above operations is O(1).

When implementing a Queue in Python, you can turn to using the `list`, `collections.deque` or the `queue.Queue`


Python offers [these](https://github.com/python/cpython/blob/main/Lib/queue.py) queues.