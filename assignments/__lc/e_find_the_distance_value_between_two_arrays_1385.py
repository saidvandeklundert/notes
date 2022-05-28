"""
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there 
is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

--

I hear now and then complains about bad explanation. 
Take your time, read slowly and literally do whatever the explanation says.

 I might take you couple minutes to understand the problem. Also, I agree, the explanation could have been better.
The problem says to count all elements in arr1 such, 
 that the difference between arr1[i] to each element in arr2 is > than d, 
 if at least one value of arr1[i] - arr2[j] <= d, then do not count that element in. 
 
 
"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for start in arr1:
            for destination in arr2:
                distance = abs(start - destination)
                if distance <= d:
                    break
            else:
                count += 1
        return count


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        for x in arr1:
            l, r = 0, len(arr2)
            while l < r:
                mid = (l + r) // 2
                if abs(arr2[mid] - x) <= d:
                    count -= 1
                    break
                elif arr2[mid] > x:
                    r = mid
                else:
                    l = mid + 1
            count += 1
        return count


alist = [
    [[4, 5, 8], [10, 9, 1, 8], 2],  # 2
    [[1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3],  # 2
    [[2, 1, 100, 3], [-5, -2, 10, -3, 7], 6],  # 1
]

for x in alist:
    print(Solution().findTheDistanceValue(x[0], x[1], x[2]))
