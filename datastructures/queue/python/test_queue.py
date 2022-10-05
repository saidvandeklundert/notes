"""
python -m pytest .
python -m mypy .
"""
from .queue import Queue


def test_create_queue():
    q = Queue()
    assert isinstance(q, Queue)


def test_enqueue():
    q = Queue()
    q.enqueue(1)

    assert q.head.value == 1
    assert q.tail.value == 1


def test_peek():
    q = Queue()
    q.enqueue(1)
    assert q.peek() == 1

    another_q = Queue()
    assert another_q.peek() is None
