"""
Return the number that is picked.
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    if num == NUM:
        return 0
    elif num < NUM:
        return 1
    elif num > NUM:
        return -1


class Solution:
    """slowwwww"""

    def guessNumber(self, n: int) -> int:

        for x in range(n + 1):
            result = guess(x)
            if result == 0:
                return x


class Solution:
    def guessNumber(self, n: int) -> int:
        i = 100
        low = 1
        high = n
        while low <= high:
            print(low, high, NUM, n)
            middle = (low + high) // 2
            result = guess(middle)
            if result == -1:  # higher
                high = middle

            elif result == 1:  # lower
                low = middle if low != middle else low + 1
            elif result == 0:  # this is it
                return middle
            i -= 1
            if i == 0:
                break


alist = [
    (10, 6),  # 6
    (1, 1),  # 1
    (2, 1),  # 1
    (2126753390, 1702766719),  # 1702766719
    (2, 2),  # 2
]

for x in alist:
    NUM = x[1]
    print("got:", Solution().guessNumber(x[0]))
