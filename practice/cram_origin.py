"""
To reset the test:

    python reset

To check the results:

    python -m pytest check.py
"""
##########
# sorting:
##########


# merge sort
# python -m pytest check.py::test_merge_sort
def mergesort(alist: list[int]) -> list[int]:
    # base case
    newlist = []

    # recursive case
    return newlist


# python -m pytest check.py::test_merging
def merging():

    return ...


# quicksort.py
# python -m pytest check.py::test_quick_sort
def quick_sort(nums, start=0, end=None):
    # base case
    pivot = partitioning()
    # recursive case


# python -m pytest check.py::test_quick_sort_partitioning
def partitioning(nums, left, right):
    return ...


############
# searching:
############


# python -m pytest check.py::test_binary_search
def binary_search(array: list[int], target: int) -> int:
    """implmenet binary search here."""

    return ...
