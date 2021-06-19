import copy
import time

from biglists import tests


def quickSort(array):
    """EZ quicksort"""
    if len(array) <= 1:
        return array

    pivot = array.pop()
    smaller = []
    bigger = []

    for i in array:
        if i < pivot:
            smaller.append(i)
        if i >= pivot:
            bigger.append(i)

    return quickSort(smaller) + [pivot] + quickSort(bigger)


def quickSortAlgo(array):
    """Solution is a lot slower BUT it is in place."""
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return

    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(pivotIdx, rightIdx, array)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def qsort(array):
    """Sort the array by using quicksort from stackoverflow
    https://stackoverflow.com/questions/18262306/quicksort-with-python
    """

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return (
            qsort(less) + equal + qsort(greater)
        )  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


if __name__ == "__main__":
    print("num0")
    i = 0

    print(f"Test number {i}")
    t1_start = time.time()
    quickSort(copy.copy(tests[0]))
    t1_finish = time.time()
    print("num1")
    i += 1
    print(f"Test number {i}")
    t2_start = time.time()
    quickSortAlgo(copy.copy(tests[0]))
    t2_finish = time.time()

    print("num2")

    i += 1
    print(f"Test number {i}")
    t3_start = time.time()
    sorted(copy.copy(tests[0]))
    t3_finish = time.time()
    i += 1
    print(f"Test number {i}")
    t4_start = time.time()
    copy.copy(tests[0]).sort()
    t4_finish = time.time()
    t5_start = time.time()
    qsort(copy.copy(tests[0]))
    t5_finish = time.time()
    print("my quicksort:", t1_finish - t1_start)
    print("algoexpert quicksort:", t2_finish - t2_start)
    print("qSort from stackoverflow as method on the list:", t5_finish - t5_start)
    print("Timsort:", t3_finish - t3_start)
    print("Timsort as method on the list:", t4_finish - t4_start)
