from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array = []
        i = 2
        while i > 0:
            i -= 1
            for num in nums:
                new_array.append(num)
        return new_array


if __name__ == "__main__":
    alist = [[1, 2, 1], [1, 3, 2, 1]]
    for nums in alist:
        print(Solution().getConcatenation(nums))
