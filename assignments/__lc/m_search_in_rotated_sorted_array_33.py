from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left, right = 0, n - 1
        # zero length array, return immediately:
        if n == 0:
            return -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid

            # pivot index / inflection point to the right:
            if arr[mid] >= arr[left]:
                # if left and middle are smaller then target,
                # set right to middle -1
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                # if left and middle are bigger then target,
                # set left to middle +1
                else:
                    left = mid + 1

            # pivot index / inflection point to the left:
            else:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPeakIndex(nums):
            # use binary search to find the max value's index
            left, right = 0, len(nums) - 1
            if len(nums) == 1:
                return 0
            if nums[0] < nums[-1]:
                return len(nums) - 1

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] > nums[mid + 1]:
                    return mid

                if (
                    nums[mid] < nums[left]
                ):  # if mid is smaller than left, max is on the left hand side
                    right = mid
                else:  # mid is greater than left, then max is on the right hand side
                    left = mid + 1

        def binarySearch(nums, target, shift):
            # given a monotonically increasing list, find the index of target + shift
            # return -1 if target does not exist

            left, right = 0, len(nums)

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid + shift

                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return -1

        peak = findPeakIndex(nums)
        left_nums = nums[0 : peak + 1]
        right_nums = nums[peak + 1 :]

        if target >= nums[0] and target <= nums[peak]:
            return binarySearch(left_nums, target, 0)
        else:
            return binarySearch(right_nums, target, peak + 1)


alist = [
    [
        [4, 5, 6, 7, 0, 1, 2],
        0,  # 4
    ],
    [
        [4, 5, 6, 7, 0, 1, 2],
        3,  # -1
    ],
    [
        [1],
        0,  # -1
    ],
]

for x in alist:
    print(Solution().search(x[0], x[1]))
