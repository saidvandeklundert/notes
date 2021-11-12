# Select the array using the Selection Sort algorithm
tests = [
    [8, 5, 2, 9, 5, 6, 3],
    [1, 3, 2],
    [-4, 5, 10, 8, -10, -6, -24, -2, -5, 3, 5, -4, -5, -1, 11, 6, -7, -6, -7, 8],
]

# O(n^2) time
# O(1) space due to in place operation of the array
def selectionSort(array):
    index = 0

    # len(array) - 1 bc when we reach the final number, the unsorted sublist is only 1 item so we can skip it
    while index < len(array) - 1:
        indexSmallest = index
        for i in range(index + 1, len(array)):
            if array[indexSmallest] > array[i]:
                indexSmallest = i
        swap(index, indexSmallest, array)
        index += 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


if __name__ == "__main__":

    for index, test in enumerate(tests):

        print(f"Test number {index +1}")
        print(selectionSort(test))
