from E06_paramatrization import multiply
from test_06_data import TEST_DATA
import pytest


def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(3, 1) == 3
    assert multiply(10, 10) == 100


# also nice is to zip a list to paramatrize 2 lists
@pytest.mark.parametrize(
    "x, y, ret",
    [
        (2, 2, 4),
        (2, 10, 20),
        (10, 10, 100),
    ],
)
def test_multiply_using_paramatrization(x, y, ret):
    assert multiply(x, y) == ret


# importing data under test:
@pytest.mark.parametrize(
    "x, y, expected",
    TEST_DATA,
)
def test_multiply_using_paramatrization_data(x, y, expected):
    assert multiply(x, y) == expected


# stacking paramatrization decorator:
@pytest.mark.parametrize(
    "y",
    [
        (1),
        (2),
        (3),
        (4),
        (5),
        (6),
        (7),
        (8),
        (9),
    ],
)
@pytest.mark.parametrize(
    "x",
    [
        (1),
        (2),
        (3),
        (4),
        (5),
        (6),
        (7),
        (8),
        (9),
    ],
)
def test_multiply_stacked_paramatrization(x, y):
    """
    Not testing for output, just testing that the func can run
    without throwing errors."""
    assert isinstance(multiply(x, y), int)
