import pytest
from .queue_linked import LinkedQueue


@pytest.fixture
def lq():
    return LinkedQueue()


def test_queue_creation():
    lq = LinkedQueue()
    assert isinstance(lq, LinkedQueue)


def test_queue_enqueue(lq: LinkedQueue):
    assert lq.is_empty() is True
    lq.enqueue(1)
    assert lq.peek() == 1
    lq.enqueue(2)
    lq.enqueue(3)
    assert lq.peek() == 1
    assert lq.rear() == 3
    assert lq.is_empty() is False


def test_queue_dequeue(lq: LinkedQueue):
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    assert lq.dequeue() == 1
    assert lq.dequeue() == 2
    assert lq.dequeue() == 3
    assert lq.dequeue() is None
