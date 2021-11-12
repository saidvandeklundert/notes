import ipdb

tests = [
    [-1, -5, -10, -1100, -1100, -1101, -1102, -9001],
    [1, 2, 0],
    [1, 1, 1, 2, 3, 4, 1],
]


def isMonotonic(array: list[int]):
    print(array)
    if len(array) == 1 or len(array) == 0:
        return True

    if array[1] > array[0]:
        c = "gt"
    elif array[1] < array[0]:
        c = "lt"
    else:
        if array[2] > array[1]:
            c = "gt"
        elif array[2] < array[1]:
            c = "lt"
        else:
            if array[3] > array[2]:
                c = "gt"
            elif array[3] < array[2]:
                c = "lt"
            else:
                c = "eq"
    i = 2

    while i < len(array):
        print("while")
        res = check(array[i - 1], array[i], c)
        print(f"res {res}")
        if not res:
            return False
        i += 1

    return True


def check(a, b, check):
    if a == b:
        return True
    elif check == "gt":
        print(f"checking gt a {a} b {b}")
        return a < b
    elif check == "lt":
        print(f"checking lt a {a} b {b}")
        return a > b
    raise ValueError(f"check input unexpected {a}{b}{check}")


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(isMonotonic(test))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        # print(firstDuplicateValue2(test))
    print("num3")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        # print(firstDuplicateValue3(test))
