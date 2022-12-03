from itertools import chain
import copy

inputs = [
    {"array": [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]},
    {"array": [[1]]},
    {"array": [[1, 2], [4, 3]]},
    {"array": [[1, 2, 3], [8, 9, 4], [7, 6, 5]]},
    {
        "array": [
            [19, 32, 33, 34, 25, 8],
            [16, 15, 14, 13, 12, 11],
            [18, 31, 36, 35, 26, 9],
            [1, 2, 3, 4, 5, 6],
            [20, 21, 22, 23, 24, 7],
            [17, 30, 29, 28, 27, 10],
        ]
    },
    {
        "array": [
            [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
            [12, 19, 15, 16, 20, 18, 13, 17, 11, 14],
        ]
    },
    {
        "array": [
            [27, 12, 35, 26],
            [25, 21, 94, 11],
            [19, 96, 43, 56],
            [55, 36, 10, 18],
            [96, 83, 31, 94],
            [93, 11, 90, 16],
        ]
    },
    {"array": [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]]},
    {"array": [[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]]},
    {
        "array": [
            [1, 11],
            [2, 12],
            [3, 13],
            [4, 14],
            [5, 15],
            [6, 16],
            [7, 17],
            [8, 18],
            [9, 19],
            [10, 20],
        ]
    },
    {"array": [[1, 3, 2, 5, 4, 7, 6]]},
    {"array": [[1], [3], [2], [5], [4], [7], [6]]},
    {"array": [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]},
]


def spiralTraverse(array):
    print("array", array)
    result = []
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, (len(array[0]) - 1)

    while start_row <= end_row and start_col <= end_col:
        # top border
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])
        # right border
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])
        # bottom border
        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            result.append(array[end_row][col])
        # left border
        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            result.append(array[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1
    return result


def spiralTraverse_slow(array):
    new_array = []
    print(array)
    while len(array) > 0:
        top = array.pop(0)
        if len(array) > 0:
            right = [alist.pop(-1) for alist in array if len(alist) > 0]
        else:
            right = []
        if len(array) > 0:
            bottom = array.pop(-1)
            bottom.reverse()
        else:
            bottom = []
        if len(array) > 0:
            left = [alist.pop(0) for alist in array if len(alist) > 0]
            left.reverse()
        else:
            left = []

        new_array.extend(chain(top, right, bottom, left))
        print(top, right, bottom, left)
    print(new_array)
    return new_array


if __name__ == "__main__":
    for test in inputs:
        array = test["array"]
        print(spiralTraverse_slow(copy.deepcopy(array)))
        print(spiralTraverse(copy.deepcopy(array)))
        print(50 * "_")
