# Queue

A Queue is a linear data structure where items are typically stored first in first out. The item that is inserted first will be removed first, just like people waiting in line for something.

Common queue operations are:
- queueu(): create a new queue
- enqueue O(1): add element to the end of the queue
- dequeue O(1): remove an element from the queue 
- front O(1): return the first element
- rear O(1): return the last element
- is_empty(): check if the queue is empty
- size(): return the size of the queue



When implementing a Queue in Python, you can turn to using the `list`, `collections.deque` or the `queue.Queue`


Python offers [these](https://github.com/python/cpython/blob/main/Lib/queue.py) queues.