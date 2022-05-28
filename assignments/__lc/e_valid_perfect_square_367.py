class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [1, 2]:
            return True
        low = 0
        high = num
        while low <= high:
            middle = (low + high) // 2
            if middle**2 == num:
                return True
            elif middle**2 > num:
                high = middle - 1
            else:
                low = middle + 1
        return False


alist = [16, 14, 1]
for x in alist:
    print(Solution().isPerfectSquare(x))
