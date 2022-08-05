def partition_begin(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort_in_place_begin_partition(array, begin=None, end=None):

    if begin is None:
        begin = 0
    if end is None:
        end = len(array) - 1

    if begin >= end:
        return

    pivot = partition_begin(array, begin, end)

    quicksort_in_place_begin_partition(array, begin, pivot - 1)
    quicksort_in_place_begin_partition(array, pivot + 1, end)
