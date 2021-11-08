try:
    import ssa
except:
    pass

inputs = [
    [1, 2, 3, 5, 6, 8, 9],
    [-5, -4, -3, -2, -1],
    [-7, -3, 1, 9, 22, 30],
]

# O(nlogn) time (we iterate the array and in the end, we also sort it)
# O(n) space: we need to create a new array
def sortedSquaredArray(array):
    new_array = []

    for i in array:
        new_array.append(i ** 2)
    new_array.sort()
    return new_array


def sorted_squared_array_optimized(array):
    new_array = [0 for _ in array]
    start_index = 0
    end_index = len(array) - 1

    for idx in reversed(range(len(array))):

        start_v = array[start_index]
        end_v = array[end_index]

        if abs(start_v) > abs(end_v):
            new_array[idx] = start_v * start_v
            start_index += 1
        else:  # needs to be else, otherwise we skip the value where start_index and end_index meet.
            new_array[idx] = end_v * end_v
            end_index -= 1
    return new_array


if __name__ == "__main__":
    for test in inputs:
        print("Python:", sortedSquaredArray(test))
        try:
            print("Rust:", ssa.sorted_squared_array(test))
        except:
            pass
        print("Python optimized:", sorted_squared_array_optimized(test))
        try:
            print("Rustoptimized:", ssa.sorted_squared_array_optimized(test))
        except:
            pass
