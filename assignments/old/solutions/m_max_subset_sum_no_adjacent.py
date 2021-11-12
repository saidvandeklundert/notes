# Select the array using the Selection Sort algorithm
tests = [
    [75, 105, 120, 75, 90, 135],
]


# O(n) time O(n) space
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return 0

    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])

    return maxSums[-1]


if __name__ == "__main__":

    for index, test in enumerate(tests):

        print(f"Test number {index +1}")
        print(maxSubsetSumNoAdjacent(test))
