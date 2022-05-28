class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            k = (left + right) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            elif n < curr:
                right = k - 1
            else:
                left = k + 1
        return right


alist = [
    5,  # 2
    8,  # 3
    1,
]
for x in alist:
    print(Solution().arrangeCoins(x))
