from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        to_add = 0
        for index, number in enumerate(nums):
            nums[index] = number + to_add
            to_add += number
        print(nums)
        return nums


alist = [
    [1, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 1, 2, 10, 1],
]

for x in alist:
    print(Solution().runningSum(nums=x))
