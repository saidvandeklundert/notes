import rust

inputs = [
    {"number": 10},
    {"number": 11},
    {"number": 12},
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


def getNthFib_rec(number):
    if number == 2:
        return 1
    elif number == 1:
        return 0
    else:
        return getNthFib_rec(number - 1) + getNthFib_rec(number - 2)


if __name__ == "__main__":
    for test in inputs:
        print(f"input argument: {test}")
        print("Python recursive:", getNthFib_rec(**test))
        print("Rust non-recursive:", rust.get_fibonacci(**test))
        print("Rust recursive:", rust.fib_in_rust_recursive(**test))
        print(50 * "-")
