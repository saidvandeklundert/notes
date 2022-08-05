def merging(left: list[int], right: list[int]) -> list[int]:
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
