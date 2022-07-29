def mergesort(array):
    """
    Mergesort implementation.

    1. divide the list into 2 halfs
    2. recursively sort the subarrays
    3. combine the sorted subarrays by merging them

    This function divides the list into halves until we end
     up with sorted lists (of lenght 0 or 1).

    The 'merge' function that is returned merges 2 sorted
     lists.
    """
    array_len = len(array)
    if array_len == 1:
        return array
    left_half = mergesort(array[: array_len // 2])
    right_half = mergesort(array[array_len // 2 :])
    return merge(left_half, right_half)


def merge(left_half: list[int], right_half: list[int]):
    """
    Merge two lists
    """
    left_half_len = len(left_half)
    right_half_len = len(right_half)
    S, i, j = [], 0, 0
    while i < left_half_len and j < right_half_len:
        if left_half[i] <= right_half[j]:
            i, _ = i + 1, S.append(left_half[i])
        else:
            j, _ = j + 1, S.append(right_half[j])
    return S + (right_half[j:] if i == left_half_len else left_half[i:])


if __name__ == "__main__":
    lists = [
        [2, 9, 8, 5, 3, 4, 7, 6],
    ]

    for alist in lists:
        print(mergesort(alist))
