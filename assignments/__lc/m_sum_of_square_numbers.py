from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            target = c - a**2
            l, r = 0, sqrt(c)
            while l <= r:
                b = l + (r - l) // 2
                if b * b == target:
                    return True
                elif b * b > target:
                    r = b - 1
                else:
                    l = b + 1
        return False


ailst = [
    5,  # True
    3,  # False
    2,  # True
    1,  # True
]

for x in ailst:
    print(Solution().judgeSquareSum(x))
