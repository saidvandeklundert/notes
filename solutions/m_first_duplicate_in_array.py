import ipdb

tests = [
    [2, 1, 5, 2, 3, 3, 4],
    [2, 1, 5, 2, 3, 3, 4],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
]


def firstDuplicateValue(array):
    s = set()
    for v in array:
        if v in s:
            return v
        else:
            s.add(v)

    return -1


def firstDuplicateValue2(array):
    d_had = {}
    for v in array:
        if v in d_had:
            return v
        else:
            d_had[v] = True

    return -1


def firstDuplicateValue3(array):
    for index, value in enumerate(array):
        print(index)
        print(array)
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1

    return -1


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(firstDuplicateValue(test))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(firstDuplicateValue2(test))
    print("num3")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(firstDuplicateValue3(test))
