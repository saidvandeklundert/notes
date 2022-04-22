from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num == target:
                return index
            elif num > target and index in [0, 1]:
                return index
            elif num > target:
                return index
        else:
            return len(nums)


if __name__ == "__main__":
    ret = Solution().searchInsert([2, 3, 5, 6], 2)
    print(ret)
    ret = Solution().searchInsert([1, 3, 5], 4)
    print(ret)
