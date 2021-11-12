inputs = [
    {"redShirtHeights": [5, 8, 1, 3, 4], "blueShirtHeights": [6, 9, 2, 4, 5]},
    {"redShirtHeights": [6, 9, 2, 4, 5], "blueShirtHeights": [5, 8, 1, 3, 4]},
    {"redShirtHeights": [6, 9, 2, 4, 5, 1], "blueShirtHeights": [5, 8, 1, 3, 4, 9]},
    {"redShirtHeights": [6], "blueShirtHeights": [6]},
    {"redShirtHeights": [126], "blueShirtHeights": [125]},
    {"redShirtHeights": [1, 2, 3, 4, 5], "blueShirtHeights": [2, 3, 4, 5, 6]},
    {
        "redShirtHeights": [1, 1, 1, 1, 1, 1, 1, 1],
        "blueShirtHeights": [5, 6, 7, 2, 3, 1, 2, 3],
    },
    {
        "redShirtHeights": [1, 1, 1, 1, 1, 1, 1, 1],
        "blueShirtHeights": [2, 2, 2, 2, 2, 2, 2, 2],
    },
    {"redShirtHeights": [125], "blueShirtHeights": [126]},
    {
        "redShirtHeights": [19, 2, 4, 6, 2, 3, 1, 1, 4],
        "blueShirtHeights": [21, 5, 4, 4, 4, 4, 4, 4, 4],
    },
    {
        "redShirtHeights": [19, 19, 21, 1, 1, 1, 1, 1],
        "blueShirtHeights": [20, 5, 4, 4, 4, 4, 4, 4],
    },
    {"redShirtHeights": [3, 5, 6, 8, 2], "blueShirtHeights": [2, 4, 7, 5, 1]},
    {"redShirtHeights": [3, 5, 6, 8, 2, 1], "blueShirtHeights": [2, 4, 7, 5, 1, 6]},
    {"redShirtHeights": [4, 5], "blueShirtHeights": [5, 4]},
    {"redShirtHeights": [5, 6], "blueShirtHeights": [5, 4]},
    {"redShirtHeights": [5, 8, 1, 3, 4], "blueShirtHeights": [6, 9, 2, 4, 5]},
]


def classPhotos_slow(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    print(redShirtHeights)
    print(blueShirtHeights)
    if redShirtHeights[0] == blueShirtHeights[0]:
        print(False)
        return False
    if redShirtHeights[0] < blueShirtHeights[0]:
        return helper(redShirtHeights, blueShirtHeights)
    else:
        return helper(blueShirtHeights, redShirtHeights)


def helper(smaller_start, longer_start):
    for idx, value in enumerate(smaller_start):
        if value < longer_start[idx]:
            continue
        else:
            print(False)
            return False
    print(True)
    return True


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirt_color_in_first_row = (
        "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
    )

    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirt_color_in_first_row == "RED":
            if redShirtHeight > blueShirtHeight:
                return False
        else:
            if blueShirtHeight > redShirtHeight:
                return False

    return True


if __name__ == "__main__":
    for test in inputs:
        print(classPhotos_slow(**test))
        print(50 * "_")
        print(classPhotos(**test))
        print(50 * "_")
