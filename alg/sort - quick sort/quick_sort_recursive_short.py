"""

in qs:
- the base case:
    here l >= r, which means there is 1 element only. And by definition, this is sorted.
- the partition
"""


def quicksort(arr):
    """Recursive implementation of quicksort"""
    qs(arr, 0, len(arr) - 1)


def qs(arr, l, r):
    """ """
    # base case
    if l >= r:
        return

    # partition
    p = partition(arr, l, r)

    # recurse both sub-arrays:
    qs(arr, l, p - 1)
    qs(arr, p + 1, r)


def partition(arr, l, r) -> int:
    """
    Partition function:

    Partitions the array section between indexes 'l' and 'r'.

    During this partitioning process, the following happens:
    - a pivot is chosen
    - element lower then the partition are put to the left
     of the partition
    - elements higher then the partition are put to the
     right of the partition

    The result is that the pivot is sorted in the section of the array
     specified by the 'l' and 'r' indexes.

    There are different pivot selection strategies.
    A simple one is to choose the last element.

    In this function, the subarray is altered in place.

    We iterate the array from l to r. The starting pointer is i.
    we constantly check if j is smaller then the pivot. If it is,
    we increment i and we swap the values in the array located in the
    i-th and j-th index. We also increment i to ensure that i keeps
    pointing to the last of the numbers that is lower then the pivot.

    In the end, we swap the pivot value (the last value) with the
    first value AFTER i.

    Finally, the function returns the position that the pivot ends up in.
    """
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    lists = [
        [3, 2, 1],
        [1, 2, 3],
        [],
        [3, 1, -1, 0, 2, 5],
        [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2],
        [0],
        [3, -2, -1, 0, 2, 4, 1],
        [1, 2, 3, 4, 5, 6, 7],
        [2, 2, 2, 2, 2, 2, 2],
    ]

    for alist in lists:
        print("before\n", alist)
        quicksort(alist)
        print("after\n", alist)
