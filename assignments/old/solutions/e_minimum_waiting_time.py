tests = [
    [3, 2, 1, 2, 6],
]


def minimumWaitingTime(queries):
    queries.sort()
    print(queries[:-1])
    x = 0
    z = 0
    for i in queries[:-1]:
        z = z + i
        x += z
    return x


def minimumWaitingTime_second(queries):
    queries.sort()

    wait = 0
    for i in queries[:-1]:
        addition = queries.pop(0) * len(queries)
        wait += addition

    return wait


def minimumWaitingTime_third(queries):
    queries.sort()

    wait = 0
    for i, q in enumerate(queries):
        wait += q * (len(queries) - (i + 1))

    return wait


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(minimumWaitingTime(test))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(minimumWaitingTime_second(test))