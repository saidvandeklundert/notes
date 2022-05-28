class Solution(object):
    def findMin(self, nums):
        # when there is only 1 element, return it:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # if the last element is greater than the first element, then there is no rotation.
        # # In this case, we are safe to return immediately:
        if nums[right] > nums[0]:
            return nums[0]

        # Using binary search to find the inflection point:
        while right >= left:
            mid = left + (right - left) // 2

            # If the mid element is greater then the 'mid+1' element, we found the inflection point.
            # In this case, 'mid+1' would be the lowest point:
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # If mid is lesser then 'mid-1', it means we found the smallest element:
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # The above was not satisfied, hence haven't yet found the smallest element.

            # If mid is bigger then the first element, the smallest value must be to the right:
            if nums[mid] > nums[0]:
                left = mid + 1
            # if the first element is greater then the mid, the smallest value must be to the left:
            else:
                right = mid - 1
