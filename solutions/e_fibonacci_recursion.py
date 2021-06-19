tests = [
    #    1,
    4,
    #    6,
    #    12,
    #    18,
]


def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        print(n)
        return getNthFib(n - 1) + getNthFib(n - 2)


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(getNthFib(test))
