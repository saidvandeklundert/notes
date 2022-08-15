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


def merging(left: list[int], right: list[int]) -> list[int]:
    new_list = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            to_insert = right.pop(0)
            new_list.append(to_insert)
        elif left[0] <= right[0]:
            to_insert = left.pop(0)
            new_list.append(to_insert)
    if len(left) > 0:
        for i in left:
            new_list.append(i)
    if len(right) > 0:
        for i in right:
            new_list.append(i)

    return new_list


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
