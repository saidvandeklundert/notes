import copy

tests = [[[3, 5, -4, 8, 11, 1, -1, 6], 10]]
# from biglists import tests


def twoNumberSum(array, targetSum):
    for index, value in enumerate(array):
        for i2, v2 in enumerate(array):
            if i2 == index:
                continue

            elif targetSum - (value + v2) == 0:
                return [value, v2]

    return []


if __name__ == "__main__":
    print("\nbinsearch\n")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(twoNumberSum(test[0], test[1]))
