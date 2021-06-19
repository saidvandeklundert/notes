import copy

tests = [
    [8, 5, 2, 9, 5, 6, 3],
]


def insertionSort(array):
    # Write your code here.
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            swap(i, i + 1, array)

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(insertionSort(copy.copy(test)))
