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
        node = Node(value=item, next=None)
        if self.tail is None:
            self.tail = node
            self.head = node

        node.next = self.tail
        self.tail = node

    def peek(self) -> Any:
        if self.head:
            return self.head.value
        return self.head
