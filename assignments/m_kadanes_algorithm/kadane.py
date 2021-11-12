inputs = [
    {"array": [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]},
    {"array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
    {"array": [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]},
    {"array": [-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]},
    {"array": [1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10]},
    {"array": [1, 2, 3, 4, 5, 6, -22, 7, 8, 9, 10]},
    {"array": [1, 2, -4, 3, 5, -9, 8, 1, 2]},
    {"array": [3, 4, -6, 7, 8]},
    {"array": [3, 4, -6, 7, 8, -18, 100]},
    {"array": [3, 4, -6, 7, 8, -15, 100]},
    {"array": [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]},
    {"array": [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 6]},
    {"array": [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6]},
    {
        "array": [
            8,
            5,
            -9,
            1,
            3,
            -2,
            3,
            4,
            7,
            2,
            -18,
            6,
            3,
            1,
            -5,
            6,
            20,
            -23,
            15,
            1,
            -3,
            4,
        ]
    },
    {
        "array": [
            100,
            8,
            5,
            -9,
            1,
            3,
            -2,
            3,
            4,
            7,
            2,
            -18,
            6,
            3,
            1,
            -5,
            6,
            20,
            -23,
            15,
            1,
            -3,
            4,
        ]
    },
    {"array": [-1000, -1000, 2, 4, -5, -6, -7, -8, -2, -100]},
    {"array": [-2, -1]},
    {"array": [-2, 1]},
    {"array": [-10]},
    {"array": [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]},
]


def kadanesAlgorithm(array):
    best = array[0]
    current_sum = array[0]
    for i in range(1, len(array)):
        num = array[i]
        current_sum = max(num, current_sum + num)
        best = max(best, current_sum)

    return best


def kadanesAlgorithm_fast(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar


if __name__ == "__main__":
    for test in inputs:
        # print(isValidSubsequence(**test))
        print(kadanesAlgorithm(**test))
        print(kadanesAlgorithm_fast(**test))
        print(50 * "_")
