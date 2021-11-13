import rust

inputs = [
    {"number": 1},
    {"number": 2},
    {"number": 3},
    {"number": 4},
    {"number": 5},
    {"number": 6},
    {"number": 7},
    {"number": 8},
    {"number": 9},
    {"number": 10},
    {"number": 11},
    {"number": 12},
    {"number": 13},
]


def getNthFib(number):
    fib_seq = [0]
    while number > 0:
        number -= 1
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
        print("Python non-recursive:", getNthFib(**test))
        print("Python recursive:", getNthFib_rec(**test))
        print("Rust non-recursive:", rust.get_fibonacci(**test))
        print("Rust recursive:", rust.fib_in_rust_recursive(**test))
        print(50 * "-")
