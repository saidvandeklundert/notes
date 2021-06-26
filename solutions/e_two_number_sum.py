tests = [
    [[3, 5, -4, 8, 11, 1, -1, 6], 10],
    [[4, 6, 1, -3], 3],
    [[4, 6, 1], 5],
]

# O(n*n) time
def twoNumberSum(array, targetSum):
    for i in array:
        for x in array:
            if x == i:
                continue
            elif i + x == targetSum:
                return [i, x]
    return []


# O(nlog(n)) time and O(1) space
def twoNumberSum_second(array, targetSum):
    array.sort()
    l = 0
    r = len(array) - 1
    while l < r:
        currSum = array[l] + array[r]
        if currSum == targetSum:
            return [array[l], array[r]]
        elif currSum < targetSum:
            l += 1
        elif currSum > targetSum:
            r -= 1


# O(n) time and O(n) space
def twoNumberSum_third(array, targetSum):
    numbers = {}

    for number in array:
        potentialMatch = targetSum - number
        if potentialMatch in numbers:
            return [potentialMatch, number]
        else:
            numbers[number] = True
    return []


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(twoNumberSum(test[0], test[1]))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(twoNumberSum_second(test[0], test[1]))
    print("num3")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(twoNumberSum_third(test[0], test[1]))
