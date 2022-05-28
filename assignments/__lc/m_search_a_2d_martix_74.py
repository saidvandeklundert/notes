from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            res = bin_search(arr, target)
            if res:
                return True
        return False


def bin_search(arr, target) -> bool:
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return True
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return False


alist = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),  # True
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),  # False
]


for x in alist:
    print(Solution().searchMatrix(x[0], x[1]))
