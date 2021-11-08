import ssa

inputs = [
    [1, 2, 3, 5, 6, 8, 9],
    [-5, -4, -3, -2, -1],
    [-7, -3, 1, 9, 22, 30],
]


def sortedSquaredArray(array):
    new_array = []

    for i in array:
        new_array.append(i ** 2)
    new_array.sort()
    return new_array


if __name__ == "__main__":
    for test in inputs:
        print("Python", sortedSquaredArray(test))
        print("Rust", ssa.sorted_squared_array(test))
