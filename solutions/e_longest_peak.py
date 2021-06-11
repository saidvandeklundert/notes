tests = [
    [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3],
]


def longestPeak(array):
    # Write your code here.

    longesPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
        # skip if current is not a peak
        if not isPeak:
            i += 1
            continue
        # check the left slope:
        leftIdx = i - 1
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        # check right slope:
        rightIdx = i + 1
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longesPeakLength = max(longesPeakLength, currentPeakLength)
        i = rightIdx

    return longesPeakLength


def testing(array):
    i = 0
    while i < len(array) - 1:
        print(i)
        print(f"index {i} value {array[i]}")
        i += 1


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(longestPeak(test))
    # testing(tests[0])
