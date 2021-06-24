import copy

tests = [
    [[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33],
    [[1, 5, 23, 111], 112],
    [[0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355],
    [[0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 0],
]
# from biglists import tests
def binarySearch(array, target):
    return binSearchHelper(array, target, 0, len(array) - 1)


def binSearchHelper(array, target, left, right):
    m = (left + right) // 2
    mv = array[m]

    if left > right:
        return -1

    if target == mv:
        return m
    elif target > mv:
        return binSearchHelper(array, target, m + 1, right)
    else:
        return binSearchHelper(array, target, left, m - 1)


if __name__ == "__main__":
    print("\nbinsearch\n")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(binarySearch(test[0], test[1]))
