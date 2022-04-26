class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n = n / 3
            print(n)

        return n == 1


if __name__ == "__main__":
    alist = [27, 0, 9, 3734, 3737]
    for x in alist:
        print(Solution().isPowerOfThree(x))
