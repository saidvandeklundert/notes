"""
python -m pytest .

Requires the following:

pip install pytest-benchmark

"""
import pytest
from .queue_linked import LinkedQueue
from .queue_circular import CircularQueue
from .queue_priority import PriorityQueue
from .queue_interface import Queue

TEST_RANGE = range(100)


@pytest.fixture
def priority_queue():
    return PriorityQueue()


@pytest.fixture
def linked_queue():
    return LinkedQueue()


@pytest.fixture
def circular_queue():
    return CircularQueue()


def test_queue_creation():
    q = LinkedQueue()
    assert isinstance(q, LinkedQueue)


@pytest.mark.parametrize(
    "q",
    [
        (LinkedQueue()),
        (CircularQueue()),
        (PriorityQueue()),
    ],
)
def test_queue_enqueue(q):
    assert q.is_empty() is True
    q.enqueue(1)
    assert q.peek() == 1
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1
    assert q.rear() == 3
    assert q.is_empty() is False


@pytest.mark.parametrize(
    "q",
    [
        (LinkedQueue()),
        (CircularQueue()),
        (PriorityQueue()),
    ],
)
def test_queue_dequeue(q: Queue):
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() is None


@pytest.mark.parametrize(
    "q",
    [
        (LinkedQueue()),
        (CircularQueue()),
        (PriorityQueue()),
    ],
)
def test_queue_front(q: Queue):
    q.enqueue(1)
    q.enqueue(2)
    front = q.front()
    assert front == 1


@pytest.mark.parametrize(
    "q",
    [
        (LinkedQueue()),
        (CircularQueue()),
        (PriorityQueue()),
    ],
)
def test_queue_rear(q: Queue):
    q.enqueue(1)
    assert q.rear() == 1
    q.enqueue(2)
    assert q.rear() == 2


@pytest.mark.parametrize(
    "q",
    [
        (LinkedQueue()),
        (CircularQueue()),
        (PriorityQueue()),
    ],
)
def test_queue_is_empty(q: Queue):
    assert q.is_empty() is True
    q.enqueue(1)
    assert q.is_empty() is False


@pytest.mark.parametrize(
    "q",
    [
        (LinkedQueue()),
        (CircularQueue()),
        (PriorityQueue()),
    ],
)
def test_queue_size(q: Queue):
    assert q.size() == 0
    q.enqueue(1)
    assert q.size() == 1


@pytest.mark.parametrize(
    "q",
    [
        (LinkedQueue()),
        (CircularQueue()),
        (PriorityQueue()),
    ],
)
def test_queue_peek(q: Queue):
    q.enqueue(1)
    q.enqueue(2)
    front = q.peek()
    assert front == 1


def test_priority_queue_priority():
    q = PriorityQueue()
    q.enqueue(100)
    q.enqueue(101)
    q.enqueue(102)
    q.enqueue(103)
    q.enqueue(104)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    val = q.dequeue()
    while True:
        old = val
        val = q.dequeue()
        if val is None:
            break
        elif val < old:
            raise ValueError("not properly prioritized!")


def linked_q():
    """
    Function that needs some serious benchmarking.
    """
    q = LinkedQueue()
    for _ in TEST_RANGE:
        q.enqueue(_)

    for _ in TEST_RANGE:
        q.dequeue()
    # You may return anything you want, like the result of a computation
    return 123


def cicular_q():
    """
    Function that needs some serious benchmarking.
    """
    q = CircularQueue()
    for _ in TEST_RANGE:
        q.enqueue(_)

    for _ in TEST_RANGE:
        q.dequeue()
    # You may return anything you want, like the result of a computation
    return 123


def test_circular_queue(benchmark):
    result = benchmark(cicular_q)


def test_linked_queue(benchmark):
    # benchmark something
    result = benchmark(linked_q)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 123


def priority_q():
    """
    Function that needs some serious benchmarking.
    """
    q = PriorityQueue()
    for _ in TEST_RANGE:
        q.enqueue(_)

    for _ in TEST_RANGE:
        q.dequeue()
    # You may return anything you want, like the result of a computation
    return 123


def test_priority_queue(benchmark):
    result = benchmark(priority_q)
