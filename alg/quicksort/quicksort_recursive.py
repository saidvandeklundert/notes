def quicksort(items: list[int], left: None | int = None, right: None | int = None):
    # default case is to have left and right span all items
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1

    print(f"quicksort called on {items[left:right+1]}")
    print(f"the full list is {items}\n\n")

    if right <= left:
        return

    # start of partitioning
    i = left
    pivot_value = items[right]

    print(f"the pivot is {pivot_value}")

    # iterat up to but not including the pivot:
    for j in range(left, right):
        # if a value is less then the pivot, swap it
        # so that it is on the left side of 'items'
        if items[j] <= pivot_value:
            # swap these two values:
            items[i], items[j] = items[j], items[i]
            i += 1

    # put the pivot on the left side of 'items'
    items[i], items[right] = items[right], items[i]

    # endd of partitioning!!!

    print(f"after swapping the range is: {items[left:right+1]}")
    print(f"recursively calling quicksort on {items[left:i]} and {items[i+1:right+1]}")

    # call quicksort on 2 partitions:
    quicksort(items, left, i - 1)  # recursive case
    quicksort(items, i + 1, right)  # recursive case


if __name__ == "__main__":
    alist = [0, 7, 6, 3, 1, 2, 5, 4]
    quicksort(alist)
    print(alist)
