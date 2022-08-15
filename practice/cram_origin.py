"""
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
def quick_sort():
    # base case
    pivot = partitioning()
    # recursive case


# python -m pytest check.py::test_quick_sort_partitioning
def partitioning(nums, left, right):
    pivot = nums[right]
    start = left - 1
    for j in range(left, right):
        if nums[j] <= pivot:
            start += 1
            nums[start], nums[j] = nums[j], nums[start]
    nums[start + 1], nums[right] = nums[right], nums[start + 1]

    return start + 1


############
# searching:
############


# python -m pytest check.py::test_binary_search
def binary_search(array: list[int], target: int) -> int:
    """implmenet binary search here."""

    return ...
