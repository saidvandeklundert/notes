inputs = [
    {"array": [75, 105, 120, 75, 90, 135]},
    {"array": []},
    {"array": [1]},
    {"array": [1, 2]},
    {"array": [1, 2, 3]},
    {"array": [1, 15, 3]},
    {"array": [7, 10, 12, 7, 9, 14]},
    {"array": [4, 3, 5, 200, 5, 3]},
    {"array": [10, 5, 20, 25, 15, 5, 5, 15]},
    {"array": [10, 5, 20, 25, 15, 5, 5, 15, 3, 15, 5, 5, 15]},
    {"array": [125, 210, 250, 120, 150, 300]},
    {"array": [30, 25, 50, 55, 100]},
    {"array": [30, 25, 50, 55, 100, 120]},
    {"array": [7, 10, 12, 7, 9, 14, 15, 16, 25, 20, 4]},
    {"array": [75, 105, 120, 75, 90, 135]},
]


def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    # copy main array
    maxSums = array[:]
    # set max value:
    maxSums[1] = max(array[0], array[1])
    print(maxSums)
    print(array)
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    print(maxSums)
    # return the last value of the array
    return maxSums[-1]


def maxSubsetSumNoAdjacentoptimized(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    second = array[0]
    first = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
        print("first", first)
        print("second", second)

    return first


if __name__ == "__main__":
    for test in inputs:
        print(maxSubsetSumNoAdjacent(**test))
        print(50 * "_")
        print(maxSubsetSumNoAdjacentoptimized(**test))
