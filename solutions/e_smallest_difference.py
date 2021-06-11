tests = [
    [[-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]],
]


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.

    results = []

    for indexO, valueO in enumerate(arrayOne):
        for indexT, valueT in enumerate(arrayTwo):
            diff = abs(valueO - valueT)
            curr = [indexO, indexT, diff]
            # print(curr)
            if len(results) > 0:
                if diff < results[2]:
                    results = curr
            else:
                results = curr

    first = results[0]
    second = results[1]
    ret_list = [arrayOne[first], arrayTwo[second]]
    return ret_list


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(smallestDifference(test[0], test[1]))
