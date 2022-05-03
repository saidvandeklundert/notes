from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        idx1 = m

        idx2 = 0

        while idx2 <= len(nums2) - 1 and idx2 <= n:
            nums1[idx1] = nums2[idx2]

            idx1 += 1
            idx2 += 1

        nums1.sort()
        print(nums1, nums2)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if the second array is empty, there's nothing to do
        if nums2:
            # pointer for each one of the arrays
            i = j = 0
            # while we don't reach the end of any of the arrays
            while i < m and j < n:
                # if the currect element of nums1 is bigger than
                #  the current element of nums2
                if nums1[i] > nums2[j]:
                    # insert the current element of nums2 into
                    #  nums1 at the position of nums1 that
                    nums1.insert(i, nums2[j])
                    # move the nums2 pointer
                    j += 1
                    # the insertion will push all elements beyond the position i to the back
                    # meaning that now the final valid element of of nums1 is at position m+1
                    m += 1
                # and we always move the nums1 pointer because either the current value of nums1
                # is in the correct position or it was moved one poistion further in the array
                # to accomodate one value from nums2
                i += 1
            # finally, if we didn't reach the end of nums2
            if j < n:
                # replace all the zeros at the end of nums1 with the rest of the values of nums2
                # that are not in nums1
                nums1[m:] = nums2[j:]
            else:
                # otherwise, we inserted all `n` elements of nums2 into nums1 and,
                # in this case, we need to delete the last `n` elements of nums1
                # (they are the zeros that we pushed back to acomodate the nums2 values)
                del nums1[-n:]


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_idx = m - 1
        nums2_idx = n - 1
        index = len(nums1) - 1
        while nums2_idx >= 0:
            if nums1_idx >= 0 and nums1[nums1_idx] > nums2[nums2_idx]:
                nums1[index] = nums1[nums1_idx]
                nums1_idx -= 1
            else:
                nums1[index] = nums2[nums2_idx]
                nums2_idx -= 1
            index -= 1


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
Solution().merge(nums1=[1], m=1, nums2=[], n=0)
