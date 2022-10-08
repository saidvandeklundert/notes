from .queue_interface import Queue
import collections


class LinkedQueue(Queue):
    def __init__(self):
        self.items = collections.deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[-1]

    def is_empty(self):
        nr_of_items = len(self.items)
        if nr_of_items == 0:
            return True
        return False

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]
