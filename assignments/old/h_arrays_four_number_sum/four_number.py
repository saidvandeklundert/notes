inputs = [
    {"array": [7, 6, 4, -1, 1, 2], "targetSum": 16},
    {"array": [1, 2, 3, 4, 5, 6, 7], "targetSum": 10},
    {"array": [5, -5, -2, 2, 3, -3], "targetSum": 0},
    {"array": [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9], "targetSum": 4},
    {"array": [-1, 22, 18, 4, 7, 11, 2, -5, -3], "targetSum": 30},
    {"array": [-10, -3, -5, 2, 15, -7, 28, -6, 12, 8, 11, 5], "targetSum": 20},
    {"array": [1, 2, 3, 4, 5], "targetSum": 100},
    {"array": [1, 2, 3, 4, 5, -5, 6, -6], "targetSum": 5},
    {
        "array": [7, 6, 4, -1, 1, 2],
        "targetSum": 16,
    },  # output should be [[7, 6, 4, -1], [7, 6, 1, 2]]
]


def fourNumberSum(array, targetSum):
    array.sort(reverse=True)
    print(array)
    print(targetSum)
    result = []
    for i in array:
        possibility = []
        target = targetSum
        possibility.append(i)
        for j in array or sum(possibility) == target:
            if j == i:
                pass
            elif sum(possibility) + j < target:
                possibility.append(j)

            if sum(possibility) == target:
                print("edding", sum(possibility))
                result.append(possibility)
    if len(result) > 0:
        print("sum", sum(result[0]))
    return result


def fourNumberSum_slow(array, targetSum):
    # Write your code here.
    pass


if __name__ == "__main__":
    for test in inputs:

        print(fourNumberSum(**test))
        print(fourNumberSum_slow(**test))
        print(50 * "_")
