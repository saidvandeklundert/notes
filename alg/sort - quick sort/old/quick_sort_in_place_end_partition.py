import copy
import time
from random import randint
import random
from typing import Callable

tests = [
    [random.randint(0, 10000000) for i in range(10000)],
]


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


def quicksort_compact(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function

    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort_compact(low) + same + quicksort_compact(high)


if __name__ == "__main__":

    in_place_arr_end_partition = copy.copy(tests[0])

    quicksort_compact_arr = copy.copy(tests[0])

    print(f"quicksort_in_place_end_partition")
    t2_start = time.time()

    quicksort_in_place_end_partition(in_place_arr_end_partition)
    t2_finish = time.time()

    print(f"quicksort_compact")
    t4_start = time.time()
    not_in_place_result = quicksort_compact(quicksort_compact_arr)
    t4_finish = time.time()

    print("quicksort_in_place_end_partition:", t2_finish - t2_start)

    print("quicksort_compact:", t4_finish - t4_start)
    assert in_place_arr_end_partition == not_in_place_result
