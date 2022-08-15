"""
python -m pytest check.py
"""

import pytest
from cram import binary_search
from cram import mergesort, merging
from cram import quick_sort, partitioning
from data import test_array_input, test_array_sorted


def test_quick_sort():
    for idx, input in enumerate(test_array_input):
        quick_sort(input)
        assert input == test_array_sorted[idx]


def test_quick_sort_partitioning():
    result = partitioning([0, 1, 2, 2, 5, 3, 4, 6, 7, 9], 4, 5)
    assert result == 4


def test_merge_sort():
    for idx, input in enumerate(test_array_input):
        input = mergesort(input)
        assert input == test_array_sorted[idx]


def test_merging():
    result = merging([0, 2, 5, 6, 8], [1, 3, 4, 7, 9])
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.parametrize(
    "array,target,expected",
    [
        ([0, 2, 14, 144, 43256, 2342366, 123124], 43256, 4),
        ([0, 2, 14, 144, 43256, 2342366, 123124], 1, -1),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 8),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 4),
        ([5], 5, 0),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ],
)
def test_binary_search(array, target, expected):
    result = binary_search(array, target)
    assert result == expected
