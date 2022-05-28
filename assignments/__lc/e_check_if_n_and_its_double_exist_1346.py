from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for index, x in enumerate(arr):
            double = 2 * x
            result = bin_search(arr, double, index)
            if result:
                return True

        return False


def bin_search(nums, target, not_allowed):
    low = 0
    high = len(nums) - 1

    while low <= high:
        # print(target, low, high, nums)
        middle = (low + high) // 2
        if nums[middle] == target and middle != not_allowed:
            return True
        elif nums[middle] == target:
            high = middle - 1
        elif nums[middle] > target:
            high = middle - 1
        elif nums[middle] < target:
            low = middle + 1
    print(target, "False", not_allowed)
    return False


alist = [
    [10, 2, 5, 3],  # True
    [7, 1, 14, 11],  # True
    [3, 1, 7, 11],  # False
    [-20, 8, -6, -14, 0, -19, 14, 4],
]
for x in alist:
    print(Solution().checkIfExist(x))
