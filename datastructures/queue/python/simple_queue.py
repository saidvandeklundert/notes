"""
Queue that is using a linked list to store all items.
"""
from __future__ import annotations
from typing import Literal, Any
from dataclasses import dataclass


@dataclass
class Node:
    value: Any
    next: Node | None


@dataclass
class Queue:
    head: Node | None = None
    tail: Node | None = None
    length: Literal[0] = 0

    def enqueue(self, item: Any):
        """
        Add an element to the queue.

        O(1)
        """
        self.length += 1
        node = Node(value=item, next=None)
        if self.tail is None:
            self.tail = node
            self.head = node

        self.tail.next = node
        self.tail = node

    def peek(self) -> Any:
        if self.head:
            return self.head.value
        return self.head

    def dequeue(self) -> Any | None:
        if self.length == 0:
            return None

        self.length -= 1
        node_to_return = self.head
        self.head = self.head.next
        return node_to_return.value

    def size(self) -> int:
        return self.length


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
