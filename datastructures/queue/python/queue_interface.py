"""
- queueu(): create a new queue
- enqueue O(1): add element to the queue
- dequeue O(1): remove an element from the queue
- front O(1): return the first element 
- rear O(1): return the last element
- is_empty O(1): check if the queue is empty
- size(): return the size of the queue
- peek(): look at the first item in the queue without removing it
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def enqueue(self, item):
        """add element to the the queue"""
        ...

    @abstractmethod
    def dequeue(self):
        """remove an element from the queue"""
        ...

    @abstractmethod
    def front(self):
        """return the first element without removing it"""
        ...

    @abstractmethod
    def rear(self):
        """return the last element without removing it"""
        ...

    @abstractmethod
    def is_empty(self):
        """check if the queue is empty"""
        ...

    @abstractmethod
    def size(self):
        """return the size of the queue"""
        ...

    @abstractmethod
    def peek(self):
        """Look at the first item in the queue without removing it"""
        ...
