tests = [
    [[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33],
    [
        [1, 5, 5, 23, 111],
        111,
    ],
]


def binarySearchRecursive(array, target):
    return binarySearchRecHelper(array, target, 0, (len(array) - 1))


def binarySearchRecHelper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    potentialMatch = array[middle]

    if target == potentialMatch:
        return "found", middle
    elif target < potentialMatch:
        return binarySearchRecHelper(array, target, left, middle - 1)
    elif target > potentialMatch:
        return binarySearchRecHelper(array, target, middle + 1, right)


def binarySearchIteratively(array, target):
    return binarySearchIterativelyHelper(array, target, 0, (len(array) - 1))


def binarySearchIterativelyHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif target < middle:
            right = middle - 1
        elif target > middle:
            left = middle + 1
    return -1


if __name__ == "__main__":
    print("recursively")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(binarySearchRecursive(test[0], test[1]))

    print("iteratively")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(binarySearchRecursive(test[0], test[1]))
