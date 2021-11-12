import copy

tests = [
    [8, 5, 2, 9, 5, 6, 3],
]
# from biglists import tests


def insertionSort(array):

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1

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
