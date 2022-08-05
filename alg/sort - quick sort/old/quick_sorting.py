# Recursive solution using a helper.
#
# Time: on average O(nlogn), worst case O(n^2)
# Space: O(n)


def quicksort(array: list[int]):
    quicksort_helper(array, 0, len(array) - 1)
    return array


def quicksort_helper(array: list[int], start: int, end: int):

    # base case
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    # Check:
    # 1. left > pivot and right < pivot
    # 2. left <= pivot
    # 3. right >= pivot
    while right >= left:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1

    # the swap:
    array[pivot], array[right] = array[right], array[pivot]

    # the recursive call:
    quicksort_helper(array, start, right - 1)
    quicksort_helper(array, right + 1, end)


if __name__ == "__main__":
    lists = [
        [2, 9, 8, 5, 3, 4, 7, 6],
    ]

    for alist in lists:
        print(quicksort(alist))
