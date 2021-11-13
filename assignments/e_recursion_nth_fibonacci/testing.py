import rust

inputs = [
    {"n": 6},
    {"n": 1},
    {"n": 2},
    {"n": 3},
    {"n": 4},
    {"n": 5},
    {"n": 7},
    {"n": 8},
    {"n": 9},
    {"n": 10},
    {"n": 11},
    {"n": 12},
    {"n": 13},
    {"n": 14},
    {"n": 15},
    {"n": 16},
    {"n": 17},
    {"n": 18},
    {"n": 19},
]


def getNthFib(n):
    n -= 1
    fib_seq = [0]
    while n > 0:
        n -= 1
        if len(fib_seq) == 1:
            fib_seq.append(1)
        else:
            last = fib_seq[-1]
            second_to_last = fib_seq[-2]
            fib_seq.append(last + second_to_last)

    return fib_seq[-1]


def getNthFib_rec(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib_rec(n - 1) + getNthFib_rec(n - 2)


if __name__ == "__main__":
    for test in inputs:
        print(getNthFib_rec(**test))
        print(rust.fib_in_rust(**test))
        print(50 * "-")
