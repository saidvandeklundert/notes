# Queue

A Queue is a linear data structure where items are typically stored first in first out. The item that is inserted first will be removed first, just like people waiting in line for something.

Common queue operations are (BigO notations assume linked-list is used):
- queueu(): create a new queue
- enqueue O(1): add element to the queue
- dequeue O(1): remove an element from the queue 
- front O(1): return the first element without removing it
- rear O(1): return the last element without removing it
- is_empty O(1): check if the queue is empty
- size(): return the size of the queue



When implementing a Queue in Python, you can turn to using the `list`, `collections.deque` or the `queue.Queue`


Python offers [these](https://github.com/python/cpython/blob/main/Lib/queue.py) queues.


# Priority Queue (PQ)

The priority queue is like a queue except every item has a certain priority. The priority determine the order in which the elements are removed from the PQ.

PQs only supports comparable data, meaning that we have to be able to compare the data that was inserted into the PQ to be able to order them according to the priority.

A PQ generally uses a heap to ensure the items stored in it remain ordered. 

Complexity:
- binary heap construction: O(n)
- Polling: O(log(n))
- Peeking: O(1)
- Adding: O(log(n))