inputs = [
    {
        "redShirtSpeeds": [5, 5, 3, 9, 2],
        "blueShirtSpeeds": [3, 6, 7, 2, 1],
        "fastest": True,
    },
    {
        "redShirtSpeeds": [5, 5, 3, 9, 2],
        "blueShirtSpeeds": [3, 6, 7, 2, 1],
        "fastest": False,
    },
    {
        "redShirtSpeeds": [1, 2, 1, 9, 12, 3],
        "blueShirtSpeeds": [3, 3, 4, 6, 1, 2],
        "fastest": False,
    },
    {
        "redShirtSpeeds": [1, 2, 1, 9, 12, 3],
        "blueShirtSpeeds": [3, 3, 4, 6, 1, 2],
        "fastest": True,
    },
    {
        "redShirtSpeeds": [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1],
        "blueShirtSpeeds": [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32],
        "fastest": True,
    },
    {
        "redShirtSpeeds": [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1],
        "blueShirtSpeeds": [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32],
        "fastest": False,
    },
    {"redShirtSpeeds": [1], "blueShirtSpeeds": [5], "fastest": True},
    {"redShirtSpeeds": [1], "blueShirtSpeeds": [5], "fastest": False},
    {"redShirtSpeeds": [1, 1, 1, 1], "blueShirtSpeeds": [1, 1, 1, 1], "fastest": True},
    {"redShirtSpeeds": [1, 1, 1, 1], "blueShirtSpeeds": [1, 1, 1, 1], "fastest": False},
    {
        "redShirtSpeeds": [1, 1, 1, 1, 2, 2, 2, 2, 9, 11],
        "blueShirtSpeeds": [1, 1, 1, 1, 3, 3, 3, 3, 5, 7],
        "fastest": True,
    },
    {
        "redShirtSpeeds": [1, 1, 1, 1, 2, 2, 2, 2, 9, 11],
        "blueShirtSpeeds": [1, 1, 1, 1, 3, 3, 3, 3, 5, 7],
        "fastest": False,
    },
    {
        "redShirtSpeeds": [9, 8, 2, 2, 3, 5, 6],
        "blueShirtSpeeds": [3, 4, 4, 1, 1, 8, 9],
        "fastest": True,
    },
    {
        "redShirtSpeeds": [9, 8, 2, 2, 3, 5, 6],
        "blueShirtSpeeds": [3, 4, 4, 1, 1, 8, 9],
        "fastest": False,
    },
    {
        "redShirtSpeeds": [5, 4, 3, 2, 1],
        "blueShirtSpeeds": [1, 2, 3, 4, 5],
        "fastest": False,
    },
    {
        "redShirtSpeeds": [5, 4, 3, 2, 1],
        "blueShirtSpeeds": [1, 2, 3, 4, 5],
        "fastest": True,
    },
    {"redShirtSpeeds": [], "blueShirtSpeeds": [], "fastest": True},
    {
        "redShirtSpeeds": [5, 5, 3, 9, 2],
        "blueShirtSpeeds": [3, 6, 7, 2, 1],
        "fastest": True,
    },
]


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    print(fastest)

    return 0


def tandemBicycle_slow(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    total_sum = 0
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()
    for i, j in zip(blueShirtSpeeds, redShirtSpeeds):
        total_sum += max(i, j)

    return total_sum


if __name__ == "__main__":
    for test in inputs:
        print(tandemBicycle_slow(**test))

        print(50 * "_")
