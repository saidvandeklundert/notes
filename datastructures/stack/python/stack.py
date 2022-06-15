from typing import Any, Iterable, Union
from collections import deque

"""

Deque is implemented in C. To view the source,
 go to https://github.com/python:
    
    cpython/Modules/_collectionsmodule.c 


"""


class Stack:
    def __init__(self, items: Union[Iterable, None] = None):
        self._stack: deque[Any] = deque()
        if items:
            for item in items:
                self._stack.append(item)

    def push(self, item: Any) -> None:
        """Puts an item on the stack."""
        self._stack.append(item)

    def pop(self) -> Any:
        """Puts an item on the stack."""
        item = self._stack.pop()
        return item

    def peek(self) -> Any:
        """Get the first item in the stack without
        removing it."""
        item = self._stack[-1]
        return item

    def clear(self) -> None:
        """Clear the items from the stack."""
        self._stack = deque()

    def count(self, item: Any) -> int:
        """Return the amount of occurences of target item in
        the stack."""
        count = self._stack.count(item)
        return count

    def is_empty() -> bool:
        raise NotImplementedError

    def size() -> int:
        raise NotImplementedError

    def __str__(self):
        return str(self._stack)

    def __len__(self):
        """Return the amount of items currently on the stack."""
        return len(self._stack)


if __name__ == "__main__":
    s = Stack()
    for i in range(10):
        s.push(i)
