tests = [
    [5, 1, 4, 2],
    [384, 48, 64, 192, 96],
    [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]


def arrayOfProducts(array: list):
    newArray = [1 for _ in array]
    for i in range(len(array)):
        currentProduct = 1
        for j in range(len(array)):
            if i == j:
                pass
            else:
                currentProduct *= array[j]
                newArray[i] = currentProduct

    return newArray


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(arrayOfProducts(test))
    # testing(tests[0])
