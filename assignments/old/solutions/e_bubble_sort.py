import copy

tests = [
    [8, 5, 2, 9, 5, 6, 3, 100, 2, 1234, 1, 100000],
]


def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        counter += 1
        isSorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
    print(f"iterated the array {counter} number of times")
    return array


def bubbleSort_optimized(array):
    isSorted = False
    counter = 0

    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        counter += 1
        print(counter)
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def bubbleSort_2(array: list):
    b_sorted = False
    n = 0
    while not b_sorted:
        n += 1
        b_sorted = True
        for index in range(len(array) - 1):

            if array[index] > array[index + 1]:
                # we need to swap
                swap(index, index + 1, array)
                b_sorted = False

    print(f"iterated the array {n} number of times")
    return array


def bubbleSort_old(array: list):
    b_sorted = False
    n = 0
    while b_sorted is False and n < 1000:
        n += 1

        for index in range(len(array)):

            if index == 0:
                continue

            elif array[index] > array[index - 1]:
                continue

            elif array[index] < array[index - 1]:
                # we need to swap
                array[index], array[index - 1] = array[index - 1], array[index]

    return array


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(bubbleSort(copy.copy(test)))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(bubbleSort_2(copy.copy(test)))
