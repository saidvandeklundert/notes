class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        for alist in grid:
            if alist[0] < 0:
                total += len(alist)

            elif alist[-1] >= 0:
                continue
            else:
                for x in alist:
                    if x < 0:
                        total += 1
        return total


from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
            l, h = 0, len(row)
            while l < h:
                m = (l + h) // 2
                if row[m] < 0:
                    h = m
                elif row[m] >= 0:
                    l = m + 1
            return len(row) - h

        count = 0
        for g in grid:

            count = count + bin(g)
        return count


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        for alist in grid:
            if alist[0] < 0:
                total += len(alist)

            elif alist[-1] >= 0:
                continue
            else:
                total += bin_search(alist)
        return total


def bin_search(nums):
    low = 0
    high = len(nums)

    while low < high:

        m = (low + high) // 2
        print(nums, low, high, m)
        if nums[m] < 0:

            high = m
        elif nums[m] >= 0:
            low = m + 1

    return len(nums) - high


alist = [
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],  # 8
    [[3, 2], [1, 0]],  # 0
    [[5, 1, 0], [-5, -5, -5]],  # 3
]

for l in alist:
    print(Solution().countNegatives(l))
