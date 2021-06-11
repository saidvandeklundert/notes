tests = [
    [[2, 1, 2, 2, 2, 3, 4, 2], 2],
    [[5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], 5],
    [[5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5],
]


def moveElementToEnd(array, toMove):
    # Write your code here.
    z = array.copy()
    counter = 0

    for index in range(len(array) - 1):

        if array[index - counter] == toMove:
            del array[index - counter]
            array.append(toMove)
            counter += 1

    print(z)
    print(array)


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(moveElementToEnd(test[0], test[1]))
