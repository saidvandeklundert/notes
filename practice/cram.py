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
    if end is None:
        end = len(nums) - 1

    if end <= start:
        return
    # base case
    pivot = partitioning(nums, start, end)
    # recursive case
    quick_sort(nums, start, pivot - 1)
    quick_sort(nums, pivot + 1, end)


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

    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1
