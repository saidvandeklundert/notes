import math


def mergesort(items: list[int]):
    print(f"merge sort called on: {items}")

    # base case: 0 or more items are naturally sorted:
    if len(items) == 0 or len(items) == 1:
        return items

    # RECURSIVE CASE - pass the left and right halves to mergesort():
    # round down if items do not deivice in half evenly:
    middle = math.floor(len(items) / 2)

    print(f"............ split into {items[:middle]} and {items[middle:]}")

    left = mergesort(items[:middle])
    right = mergesort(items[middle:])

    # Base case: returned merged, sorted data
    # at this point, left should be sorted and right
    # should be sorted. We can merge them into
    # a single sorted list.
    print(f"............ left {left} right {right} len(items) {len(items)}")
    sorted_result = []
    ileft = 0
    iright = 0
    while len(sorted_result) < len(items):
        # append the smaller value to sorted_result
        if left[ileft] < right[iright]:
            sorted_result.append(left[ileft])
            ileft += 1
        else:
            sorted_result.append(right[iright])
            iright += 1

        # if one of the pointers reached the end of the list
        # put the rest of the other list into sortedResult
        if ileft == len(left):
            sorted_result.extend(right[iright:])
            break
        elif iright == len(right):
            sorted_result.extend(left[ileft:])
            break

    print(f"The two halves {right} and {left} merged into : {sorted_result}")

    return sorted_result  # return a sorted version of items


if __name__ == "__main__":
    alist = [2, 9, 8, 5, 3, 4, 7, 6]
    sorted_list = mergesort(alist)
    print(sorted_list)
