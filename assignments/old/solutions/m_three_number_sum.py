tests = [
    [[12, 3, 1, 2, -6, 5, -8, 6], 0],
]


def threeNumberSum(array, targetSum):
    # shamebell
    ret = []

    for v1 in array:
        for v2 in array:
            for v3 in array:
                if v1 == v2:
                    continue
                elif v2 == v3:
                    continue
                elif v1 == v3:
                    continue
                elif (v1 + v2 + v3) == targetSum:
                    addition = [v1, v2, v3]
                    addition.sort()
                    if not addition in ret:
                        ret.append(addition)
    ret.sort()
    return ret


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(threeNumberSum(test[0], test[1]))
