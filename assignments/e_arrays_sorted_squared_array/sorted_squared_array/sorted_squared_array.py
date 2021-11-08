import ssa

inputs = [
    [1, 2, 3, 5, 6, 8, 9],
]


def sortedSquaredArray(array):
    new_array = []

    for i in array:
        new_array.append(i ** 2)
    return new_array


if __name__ == "__main__":
    for test in inputs:
        print(sortedSquaredArray(test))
    for test in inputs:
        print(ssa.sorted_squared_array(test))