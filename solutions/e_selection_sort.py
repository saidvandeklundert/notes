# Select the array using the Selection Sort algorithm
tests = [
    [8, 5, 2, 9, 5, 6, 3],
    [1, 3, 2],
]


def selectionSort(array):
    # Write your code here.
    currentIdx = 0

    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def selectSort(array):
    i = 0

    while i < len(array) - 1:
        smallest = i
        for i in range(i + 1, len(array)):
            if array[i] > array[smallest]:
                smallest = i
            swap(smallest, i, array)
    return array


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(selectionSort(test))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(selectSort(test))
