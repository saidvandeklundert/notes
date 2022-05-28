from typing import Tuple, List


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        arr = []
        for idx, lst in enumerate(mat):
            strength = bin_search(lst)
            arr.append((strength, idx))
        arr.sort()
        print("k", k)
        ret = [x[1] for x in arr]
        return ret[:k]


def bin_search(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (low + high) // 2

        if nums[middle] == 1:

            low = middle + 1
        elif nums[middle] == 0:
            high = middle - 1
    return low


print(
    Solution().kWeakestRows(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
        3,
    )
)

print(
    Solution().kWeakestRows(
        [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]],
        2,
    )
)
