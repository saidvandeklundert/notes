# Recursive Python Program for merge sort:


def merging(left: list[int], right: list[int]) -> list[int]:
    """Merging function"""
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


def mergesort(alist: list[int]) -> list[int]:
    newlist = []
    if len(alist) == 1:
        newlist = alist
    else:
        half = len(alist) // 2
        left = mergesort(alist[:half])
        right = mergesort(alist[half:])
        newlist = merging(left, right)
    return newlist


if __name__ == "__main__":
    newcabinet = []
    left = [1, 3, 4, 4, 5, 7, 8, 9]
    right = [2, 4, 6, 7, 8, 8, 10, 12, 13, 14]
    right = [12, 14, 555, 123123, 2, 42323, 6, 7, 8, 8, 10]
    print(merging(left, right))

    print(mergesort([9, 2, 3, 6, 34, 564, 234, 2, 3, 455, 343555]))
