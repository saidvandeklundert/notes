"""
python -m pytest exception_testing.py
"""
import pytest


def test_zero_division():
    """
    This test case will pass in case a ZeroDivisionError is
    raised during test execution inside the 'with' block.
    """
    with pytest.raises(ZeroDivisionError):
        1 / 0
