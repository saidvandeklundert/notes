from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        nums_length = len(nums)

        if nums_length <= nums[0]:  # length is smaller then the first number:
            return nums_length

        for i in range(1, nums_length):
            # counts number of elements in nums greater than equal i
            count = nums_length - i
            if nums[i] >= count and count > nums[i - 1]:
                return count
        return -1


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        k = -1
        while k <= len(nums):
            count = 0
            for i in nums:
                if i >= k:
                    count += 1
            if k == count:
                return k
            k += 1
        return -1


from collections import Counter


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count, nums = 0, Counter(nums)
        for i in range(max(nums), -1, -1):
            count += nums[i]
            if count == i:
                return count
        return -1


# nums is special if x is such that there are exactly x numbers in nums that are greater than or equal to x
#
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # sort the array:
        nums.sort()

        # if the lenght of the array is equal to or smaller than
        #  the first entry, return
        if len(nums) <= nums[0]:
            return len(nums)

        # binsearch:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            x = len(nums) - mid  # x is number of numbers bigger than mid

            # mid is greater than or equal to x
            if nums[mid] >= x:
                # if everything to the left of mid is smaller then x, return x
                if nums[mid - 1] < x:
                    print("nums,nums[mid - 1],x")
                    print(nums, nums[mid - 1], x)
                    return x
                # left of mid is not smaller than x,
                # decrement high
                else:
                    high = high - 1
            else:
                # since mid is not equal to or bigger than x,
                #  increment low to see if we can find
                #  a place where mid is higher than x.
                low = low + 1

        # the bin_search did not yield any results:
        return -1


alist = [
    [3, 5],  # 2
    [0, 0],  # -1
    [0, 4, 3, 0, 4],  # 3
    [0, 4, 3, 0, 4],  # 3
]

for x in alist:
    print(Solution().specialArray(x))
