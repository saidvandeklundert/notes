inputs = [
    {"array": [2, 3, 1, -4, -4, 2]},
    {"array": [2, 2, -1]},
    {"array": [2, 2, 2]},
    {"array": [1, 1, 1, 1, 1]},
    {"array": [-1, 2, 2]},
    {"array": [0, 1, 1, 1, 1]},
    {"array": [1, 1, 0, 1, 1]},
    {"array": [1, 1, 1, 1, 2]},
    {"array": [3, 5, 6, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]},
    {"array": [3, 5, 5, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]},
    {"array": [1, 2, 3, 4, -2, 3, 7, 8, 1]},
    {"array": [1, 2, 3, 4, -2, 3, 7, 8, -8]},
    {"array": [1, 2, 3, 4, -2, 3, 7, 8, -26]},
    {"array": [10, 11, -6, -23, -2, 3, 88, 908, -26]},
    {"array": [10, 11, -6, -23, -2, 3, 88, 909, -26]},
    {"array": [1, -1, 1, -1]},
    {"array": [2, 3, 1, -4, -4, 2]},
    {"array": [3, 5, 5, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]},
]


def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0

    while numElementsVisited < len(array):
        if numElementsVisited > 1 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)

    # if we made a cycle, then the currIdx is
    #  back at the starting point
    return currentIdx == 0


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    # [26, 1, 2, 3, 4]
    # nextIdx = (0+26) % 5 --> 1
    #
    #
    # Next is necessary in other languages where negative
    #  numbers can result in a negative modulo.
    # In Python, that is not possible.
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


def hasSingleCycle_slow(array):
    # Write your code here.
    pass


if __name__ == "__main__":
    for test in inputs:

        # print(hasSingleCycle_slow(**test))
        print(hasSingleCycle(**test))

        print(50 * "_")
