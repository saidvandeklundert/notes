from queue_interface import Queue
import numpy


class CircularQueue(Queue):
    def __init__(self, capacity: int = 100):
        self.items = numpy.zeros(capacity, dtype=int)
        self.length = capacity
        self.head = -1
        self.tail = -1

    def enqueue(self, item):
        if (self.tail + 1) % self.length == self.head:
            raise ValueError("Queue is full")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.items[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.length
            self.items[self.tail] = item

    def dequeue(self):
        if self.head == -1:
            # raise ValueError("Queue is empty")
            return None
        elif self.head == self.tail:
            return_item = self.items[self.head]
            self.head = -1
            self.tail = -1
            return return_item
        else:
            return_item = self.items[self.head]
            self.head = (self.head + 1) % self.length
            return return_item

    def front(self):
        return self.items[self.head]

    def rear(self):
        return self.items[self.tail]

    def is_empty(self):
        if self.head == -1 and self.tail == -1:
            return True
        return False

    def size(self):
        if self.is_empty():
            return 0
        # elif self.head == 0 and self.tail == 0:
        #    return 1
        return self.tail - self.head + 1

    def peek(self):
        return self.items[self.head]


if __name__ == "__main__":
    q = CircularQueue(10)
    print("size", q.size())
    q.enqueue(1)
    print("size", q.size())
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print("size", q.size())
    print(q.items)
    print("Going to dequeue")

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.items)
    print(q.head)
    print(q.tail)
