inputs = [
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 33},
    {"array": [1, 5, 23, 111], "target": 111},
    {"array": [1, 5, 23, 111], "target": 5},
    {"array": [1, 5, 23, 111], "target": 35},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 0},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 1},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 21},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 45},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 61},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 71},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 72},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 73},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 70},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], "target": 355},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], "target": 354},
    {"array": [1, 5, 23, 111], "target": 120},
    {"array": [5, 23, 111], "target": 3},
    {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 33},
]


def binarySearch_slow(array, target):
    return helper(array, target, 0, len(array) - 1)


def helper(array, target, left, right):
    # print(array, target, left, right)
    if left > right:
        return -1
    middle = (left + right) // 2
    # print("middle", middle)

    if array[middle] == target:
        return middle
    elif array[middle] > target:
        # print(array[middle])
        right = middle
        return helper(array, target, left, (middle - 1))
    elif array[middle] < target:
        # print(array[middle])
        left = middle
        return helper(array, target, (middle + 1), right)


def binarySearch(array, target):
    # set the left and right pointer to encompass the entire array
    return bin_helper(array, target, 0, len(array) - 1)


def bin_helper(array, target, left, right):
    # value does not exist here:
    if left > right:
        return -1
    middle = (left + right) // 2
    if target == array[middle]:
        return middle
    elif target > array[middle]:
        return bin_helper(array, target, middle + 1, right)
    elif target < array[middle]:
        return bin_helper(array, target, left, middle - 1)


def binarySearch_std(array, target):

    import bisect

    idx = bisect.bisect_right(array, target)

    if idx <= len(array) and array[idx - 1] == target:
        return idx - 1
    else:
        return -1


if __name__ == "__main__":
    for test in inputs:
        print(binarySearch(**test))
        print(binarySearch_std(**test))
        print(binarySearch_slow(**test))
        print(50 * "_")
