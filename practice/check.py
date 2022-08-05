"""
python -m pytest check.py
"""

from merge_sort import mergesort
from quicksort import quick_sort
from data import test_array_input, test_array_sorted


def test_quick_sort():
    for idx, input in enumerate(test_array_input):
        quick_sort(input)
        assert input == test_array_sorted[idx]


def test_merge_sort():
    for idx, input in enumerate(test_array_input):
        input = mergesort(input)
        assert input == test_array_sorted[idx]
