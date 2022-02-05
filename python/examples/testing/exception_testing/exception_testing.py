"""
python -m pytest .\exception_testing.py
"""

def test_zero_division_1():
    with pytest.raises(ZeroDivisionError):
        1 / 1

def test_zero_division_2():
    with pytest.raises(ValueError):
        1 / 0

def test_zero_division_2():
    with pytest.raises(ZeroDivisionError):
        1 / 0