from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        result[0] = self.findStartingIndex(nums, target)
        result[1] = self.findEndingIndex(nums, target)
        return result

    def findStartingIndex(self, nums, target):
        index = -1  # in case we do not find the target
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                index = mid  # we found the target and set it
                high = mid - 1  # now we see if there is anything to the left

            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index  # return the index, whether we find it or not

    def findEndingIndex(self, nums, target):
        index = -1  # in case we do not find the target
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                low = mid + 1  # now we see if there is anything to the right
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index


a = [
    [
        [5, 7, 7, 8, 8, 10],
        8,
    ],  # 3,4
    [[5, 7, 7, 8, 8, 10], 6],  # [-1,-1]
    [[], 6],  # [-1,-1]
    [
        [5, 7, 7, 8, 8, 8, 10],
        8,
    ],  # [3,5]
    [[1], 1],  #
]

for x in a:
    print(Solution().searchRange(x[0], x[1]))
