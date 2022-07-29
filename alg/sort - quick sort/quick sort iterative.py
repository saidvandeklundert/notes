from collections import deque


def swap(array: list[int], i, j):
    """swap the i and j index in an array."""
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array: list[int], start, end):

    # set the pivot
    pivot = array[end]

    # elements less than the pivot will go to the left of `pIndex`
    # elements more than the pivot will go to the right of `pIndex`
    # equal elements can go either way
    pIndex = start

    # each time we find an element less than or equal to the pivot,
    # `pIndex` is incremented, and that element would be placed
    # before the pivot.
    for i in range(start, end):
        if array[i] <= pivot:
            swap(array, i, pIndex)
            pIndex = pIndex + 1

    # swap `pIndex` with pivot
    swap(array, pIndex, end)

    # return `pIndex` (index of the pivot element)
    return pIndex


# Iterative Quicksort routine
def iterative_quicksort(array: list[int]):

    # create a stack for storing sublist start and end index
    stack = deque()

    # get the starting and ending index of a given list
    start = 0
    end = len(array) - 1

    # push the start and end index of the array into the stack
    stack.append((start, end))

    # loop till stack is empty
    while stack:

        # remove top pair from the list and get sublist starting
        # and ending indices
        start, end = stack.pop()

        # rearrange elements across pivot
        pivot = partition(array, start, end)

        # push sublist indices containing elements that are
        # less than the current pivot to stack
        if pivot - 1 > start:
            stack.append((start, pivot - 1))

        # push sublist indices containing elements that are
        # more than the current pivot to stack
        if pivot + 1 < end:
            stack.append((pivot + 1, end))


if __name__ == "__main__":
    lists = [
        [2, 9, 8, 5, 3, 4, 7, 6],
    ]

    for alist in lists:
        print("before\n", alist)
        iterative_quicksort(alist)
        print("after\n", alist)
