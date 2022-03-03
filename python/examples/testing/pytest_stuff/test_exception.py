import pytest


def divide(x: int, y: int) -> int:
    return x / y


def test_for_exception():
    """Following will have pytest pass the test when the code in
    the context generates a 'ZeroDivisionError'."""
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)
