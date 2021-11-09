inputs = [
    {"array": [3, 5, -4, 8, 11, 1, -1, 6], "targetSum": 10},  # [-1. 11]
    {"array": [4, 6], "targetSum": 10},
    {"array": [4, 6, 1], "targetSum": 5},
    {"array": [4, 6, 1, -3], "targetSum": 3},
    {"array": [1, 2, 3, 4, 5, 6, 7, 8, 9], "targetSum": 17},
    {"array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 15], "targetSum": 18},
    {"array": [-7, -5, -3, -1, 0, 1, 3, 5, 7], "targetSum": -5},
    {"array": [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], "targetSum": 163},
    {"array": [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], "targetSum": 164},
    {"array": [3, 5, -4, 8, 11, 1, -1, 6], "targetSum": 15},
    {"array": [14], "targetSum": 15},
    {"array": [15], "targetSum": 15},
]

# O(n)2 time, O(1) space
def twoNumberSum_slow(array, targetSum):
    """slow version, iterating the array twice"""
    for idx_1, value_i in enumerate(array):
        for idx_2, value_j in enumerate(array):
            if value_i + value_j == targetSum and idx_1 != idx_2:
                return [value_i, value_j]
    return []


# O(n) time, we iterate the entire array
# O(n) space (we create a hashtable)
def twoNumberSum(array, targetSum):
    seen = {}
    seen[array.pop()] = True
    for v in array:
        if targetSum - v in seen:
            return [v, (targetSum - v)]
        else:
            seen[v] = True

    return []


if __name__ == "__main__":
    for test in inputs:
        print(twoNumberSum_slow(**test))
        print(twoNumberSum(**test))