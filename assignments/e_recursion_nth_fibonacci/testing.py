import rust

inputs = [
    {"n": 10},
    {"n": 11},
    {"n": 12},
]


def getNthFib_rec(n):
    print(n)
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib_rec(n - 1) + getNthFib_rec(n - 2)


if __name__ == "__main__":
    for test in inputs:
        print(f"{test}")
        print(getNthFib_rec(**test))
        print(rust.fib_in_rust(**test))
        print(50 * "-")
