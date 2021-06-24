import copy

tests = [
    [[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33],
    [[1, 5, 23, 111], 112],
    [[0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355],
    [[0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 0],
]
# from biglists import tests


def binarySearch(array, target):
    return binHelper(array, target, 0, len(array) - 1)


def binHelper(array, target, left, right):
    if left > right:
        return -1

    m = (left + right) // 2
    mv = array[m]

    if target == mv:
        return m
    elif target > mv:
        return binHelper(array, target, m + 1, right)
    else:

        return binHelper(array, target, left, m - 1)


def linear(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1


def py_bisect_left(array, target):
    import bisect

    # bisec_left: start search at left-side of the array
    # bisec_right or bisect: start search at right-side of the array
    # both return the index where something should be inserted
    # when using bisect/bisect_right, deduct 1 from the returned index when
    # checking to see if that is the actual value
    idx = bisect.bisect_left(array, target)

    if idx < len(array) and array[idx] == target:
        return idx
    else:
        return -1


def py_bisect_right(array, target):
    import bisect

    idx = bisect.bisect_right(array, target)

    if idx <= len(array) and array[idx - 1] == target:
        return idx - 1
    else:
        return -1


if __name__ == "__main__":
    print("\nbinsearch\n")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(binarySearch(test[0], test[1]))
    print("\nlinear\n")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(linear(test[0], test[1]))
    print("\nbisect left\n")

    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(py_bisect_left(test[0], test[1]))
    print("\nbisect right\n")

    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(py_bisect_right(test[0], test[1]))
