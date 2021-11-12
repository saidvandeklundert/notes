inputs = [
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [5, 1, 22, 25, 6, -1, 8, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [5, 1, 22, 6, -1, 8, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [22, 25, 6]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [5, 1, 22, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [5, -1, 8, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [25]},
    {"array": [1, 1, 1, 1, 1], "sequence": [1, 1, 1]},
    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 12],
    },
    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [4, 5, 1, 22, 25, 6, -1, 8, 10],
    },
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [5, 1, 22, 23, 6, -1, 8, 10]},
    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 22, 25, 6, -1, 8, 10],
    },
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [5, 1, 22, 22, 6, -1, 8, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, -1]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, -1, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, -2]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [26]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [5, 1, 25, 22, 6, -1, 8, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [5, 26, 22, 8]},
    {"array": [1, 1, 6, 1], "sequence": [1, 1, 1, 6]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, 10, 11, 11, 11, 11]},
    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 10],
    },
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, 10]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, -1]},
    {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, 10]},
]


def isValidSubsequence_while(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)


def isValidSubsequence(array, sequence):
    target = 0
    for i in array:
        # print(f"target: {target} len sequence{len(sequence)}")
        if target == len(sequence):
            return True
        elif i == sequence[target]:
            # print(f"{i} == {sequence[target]}")
            target += 1
    if target == len(sequence):
        return True
    else:
        return False


if __name__ == "__main__":
    for test in inputs:
        # print(isValidSubsequence(**test))
        print(isValidSubsequence(**test))
        print(isValidSubsequence_while(**test))
        print(50 * "_")
