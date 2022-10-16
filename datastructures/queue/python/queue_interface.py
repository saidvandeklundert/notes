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
from typing import TypeVar

T = TypeVar("T")
from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def enqueue(self, item: T) -> None:
        """add element to the the queue"""
        ...

    @abstractmethod
    def dequeue(self) -> T | None:
        """remove an element from the queue"""
        ...

    @abstractmethod
    def front(self) -> T | None:
        """return the first element without removing it"""
        ...

    @abstractmethod
    def rear(self) -> T | None:
        """return the last element without removing it"""
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        """check if the queue is empty"""
        ...

    @abstractmethod
    def size(self) -> int:
        """return the size of the queue"""
        ...

    @abstractmethod
    def peek(self) -> T | None:
        """Look at the first item in the queue without removing it"""
        ...
