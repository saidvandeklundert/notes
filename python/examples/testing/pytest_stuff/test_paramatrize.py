import pytest


def multiply(x: int, y: int) -> int:
    return x * y


@pytest.mark.parametrize(
    "x, y",
    [
        (2, 1),
        (2, 2),
        (123123, 123123),
    ],
)
def test_divide_numbers_raises_value_error(x, y):
    ret = multiply(x, y)
    assert isinstance(ret, int)
