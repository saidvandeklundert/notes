def partition_end(array: list[int], begin: int, end: int) -> int:
    """

    Quicksort partitioning:
    1: set pivot
    2: sort the array into values lower, equal and higher then the pivot.
    3: return the pivot index

    Detailed:
    1: set pivot to the end
    2: sort the array into values lower then the pivot, equal to the pivot and higher then the pivot
      - 1: check every value against the pivot
      - 2: if the value is less then the pivot,
        swap it to the idx tracking the 'lower-then' values
      - 3: after ranging over the array, swap the first value
       after the subarray with the 'lower-then' values with the pivot
    3: return the pivot index
    """
    pivot = array[end]
    i = begin - 1
    for j in range(begin, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def quicksort_in_place_end_partition(array, begin=None, end=None):
    """
    This version of quicksort is performing everything 'in-place'.

    This means we use the same array and we do not require
    additional memmory."""

    if begin is None:
        begin = 0
    if end is None:
        end = len(array) - 1

    if begin >= end:
        return

    pivot = partition_end(array, begin, end)

    quicksort_in_place_end_partition(array, begin, pivot - 1)
    quicksort_in_place_end_partition(array, pivot + 1, end)
