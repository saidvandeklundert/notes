tests = [
    [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7],
]


def findThreeLargestNumbers(array):
    largestNumbers = [array[0]]

    for i in array[1::]:
        if len(largestNumbers) < 3:
            largestNumbers.append(i)
            largestNumbers.sort()

        elif i > largestNumbers[0]:
            del largestNumbers[0]
            largestNumbers.append(i)
            largestNumbers.sort()

    return largestNumbers


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(findThreeLargestNumbers(test))
    # testing(tests[0])
