from typing import List


class Solution:
    """101"""

    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        doubles = 0
        for index, number in enumerate(nums):
            if seen.get(number) is not None:

                nums[index] = "_"
                doubles += 1

            else:
                seen[number] = index

        idx = 0
        double_doubles = doubles
        for number in seen.keys():
            nums[idx] = number
            idx += 1
        while double_doubles > 0:
            double_doubles -= 1
            nums[idx] = "_"
            idx += 1

        print(nums)
        return len(nums) - doubles


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            print("checking i:", i)
            if nums[i] != nums[newTail]:
                print("i is not equal to the newtail")
                newTail += 1
                nums[newTail] = nums[i]
            else:
                print("i is equal to the newtail")
        print(nums)
        return newTail + 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        length = 0
        if len(nums) == 0:
            return length
        for i in range(1, len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length + 1


alist = [
    [1, 1, 2],  # 2
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],  # 5
]

for nums in alist:
    print(Solution().removeDuplicates(nums))
