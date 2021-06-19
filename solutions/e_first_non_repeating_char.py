tests = [
    "abcdcaf",
    "abcdbaf",
]


def nonRepeating(s):
    if len(s) <= 1:
        return -1
    seen = {}
    for i, c in enumerate(s):
        if c in seen:
            seen[c] = len(s) + 1
        else:
            seen[c] = i

    lowest = min(seen.values())

    if lowest > len(s):
        return -1
    else:
        return lowest


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(nonRepeating(test))
