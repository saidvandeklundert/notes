"""
python -m pytest .
python -m mypy .
"""
from .simple_queue import Queue
from unittest.mock import Mock


def test_create_queue():
    q = Queue()
    assert isinstance(q, Queue)


def test_enqueue():
    q = Queue()
    q.enqueue(1)

    assert q.head.value == 1
    assert q.tail.value == 1

    q.enqueue(2)
    assert q.head.value == 1
    assert q.tail.value == 2


def test_peek():
    q = Queue()
    q.enqueue(1)
    assert q.peek() == 1

    another_q = Queue()
    assert another_q.peek() is None


def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() is None


def test_size():
    q = Queue()
    assert q.size() == 0
    q.enqueue(1)
    assert q.size() == 1
    q.enqueue(2)
    assert q.size() == 2
    q.dequeue()
    assert q.size() == 1
