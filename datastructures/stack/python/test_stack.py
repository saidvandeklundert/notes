"""
python -m pytest test_stack.py
python -m mypy stack.py
"""
from stack import Stack
from collections import deque


def test_stack_creation():
    s = Stack()
    assert isinstance(s, Stack)
    s1 = Stack([1, 2, 3])
    assert isinstance(s1, Stack)


def test_stack_push():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3


def test_stack_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_stack_clear():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.clear()
    s._stack == deque()


def test_stack_count():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(2)
    s.push(2)
    s.count(1) == 1
    s.count(2) == 3


def test_len():
    s = Stack()
    s.push(1)
    s.push(2)
    assert len(s) == 2
