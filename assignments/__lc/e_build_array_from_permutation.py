from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for number in nums:
            ans.append(nums[number])
        return ans


if __name__ == "__main__":
    alist = [[0, 2, 1, 5, 3, 4], [5, 0, 1, 2, 3, 4]]
    for nums in alist:
        print(Solution().buildArray(nums))
