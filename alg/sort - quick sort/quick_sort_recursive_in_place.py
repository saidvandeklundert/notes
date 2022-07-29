import copy
import time

import random
from typing import Callable

tests = [
    [random.randint(0, 10000000) for i in range(1000000)],
]


def quicksort_not_in_place(array: list[int]):
    """Sort the array by using quicksort from stackoverflow
    https://stackoverflow.com/questions/18262306/quicksort-with-python

    This version of quicksort is NOT performing everything 'in-place'.

    This means we use additional memory.
    """

    less = []  # subarray for values less then the pivot
    equal = []  # here we store the pivot
    greater = []  # subarray for values greater then the pivot

    # partitioning:
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        # use join the return of the recursive calls to the list
        # that contains all the values equal to the pivot
        return quicksort_not_in_place(less) + equal + quicksort_not_in_place(greater)

    else:
        # the end of the recursion,
        # when there is only 1 element left:
        return array


def partition_begin(array, begin, end):
    """
    Partitioning phase where the partition is the first element.
    """
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def partition_end(array: list[int], begin: int, end: int) -> int:
    """

    Quicksort partitioning for end partition:
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


def quicksort_in_place(array) -> Callable:
    """
    This version of quicksort is performing everything 'in-place'.

    This means we use the same array and we do not require
    additional memmory."""
    begin = 0
    end = len(array) - 1

    def _quicksort(array, begin, end) -> None:
        if begin >= end:
            return
        pivot = partition_begin(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


def quicksort_in_place_end_partition(array) -> Callable:
    """
    This version of quicksort is performing everything 'in-place'.

    This means we use the same array and we do not require
    additional memmory."""
    begin = 0
    end = len(array) - 1
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end) -> None:
        if begin >= end:
            return
        pivot = partition_end(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


if __name__ == "__main__":

    in_place_arr = copy.copy(tests[0])
    in_place_arr_end_partition = copy.copy(tests[0])
    not_in_place_arr = copy.copy(tests[0])
    print(f"quicksort_in_place")
    t1_start = time.time()

    quicksort_in_place(in_place_arr)
    t1_finish = time.time()

    print(f"quicksort_in_place_end_partition")
    t2_start = time.time()

    quicksort_in_place_end_partition(in_place_arr_end_partition)
    t2_finish = time.time()

    print(f"quicksort_not_in_place")
    t3_start = time.time()
    not_in_place_result = quicksort_not_in_place(not_in_place_arr)
    t3_finish = time.time()
    print("quicksort_in_place:", t1_finish - t1_start)
    print("quicksort_in_place_end_partition:", t2_finish - t2_start)
    print("quicksort_not_in_place:", t3_finish - t3_start)
    assert not_in_place_result == in_place_arr == in_place_arr_end_partition
