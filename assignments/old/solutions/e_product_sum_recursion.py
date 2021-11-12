tests = [
    [5, 2, [7, -1], 3, [6, [-13, 8], 4]],
]

# O(n) time | O(d) space, where d is the depth of the stack
def productSum(array, multiplier=1):
    print(f"multiplier: {multiplier} array {array}")
    totalSum = 0
    for item in array:

        if type(item) == int:
            totalSum += item
        elif isinstance(item, list):
            totalSum += productSum(item, multiplier + 1)

    return totalSum * multiplier


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(productSum(test))
