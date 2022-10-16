from __future__ import annotations
from queue_interface import Queue
from typing import TypeVar
from heapq import heappop, heappush


T = TypeVar("T")


class PriorityQueue(Queue):
    def __init__(
        self,
    ):
        self.items = list()

    def enqueue(self, item: T) -> None:
        """add element to the the queue"""
        heappush(self.items, item)

    def dequeue(self) -> T | None:
        """remove an element from the queue"""
        try:
            return heappop(self.items)
        except IndexError:
            return None

    def front(self) -> T | None:
        """return the first element without removing it"""
        return self.items[0]

    def rear(self) -> T | None:
        """return the last element without removing it"""
        return self.items[-1]

    def is_empty(self) -> bool:
        """check if the queue is empty"""
        length = len(self.items)
        if length == 0:
            return True
        return False

    def size(self) -> int:
        """return the size of the queue"""
        return len(self.items)

    def peek(self) -> T | None:
        """Look at the first item in the queue without removing it"""
        return self.items[0]
