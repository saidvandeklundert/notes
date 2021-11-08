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


def sorted_squared_array_optimized(array):
    new_array = [0 for i in array]
    start = 0
    end = len(array) - 1

    while True:
        start_v = array[start] ** 2
        end_v = array[end] ** 2
        if end_v > start_v:
            new_array[end] = end_v
            end -= 1
        elif start_v > end_v:
            new_array[end] = start_v
            start += 1
        elif end_v == start_v:
            new_array[end] = end_v
            return new_array


if __name__ == "__main__":
    for test in inputs:
        print("Python:", sortedSquaredArray(test))
        print("Rust:", ssa.sorted_squared_array(test))
        print("Python optimized:", sorted_squared_array_optimized(test))
