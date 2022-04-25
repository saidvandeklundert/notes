from audioop import add
from typing import List, Optional
from unicodedata import digit


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        If the last digit is not a 9, add 1

        If the last digit is a 9, turn it into 0
         and add 1 to the second-to last digit.
        """
        print("Start")

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        digits.insert(0, 0)
        idx = len(digits) - 1

        while idx >= 0:

            print(digits[0 - idx], idx)
            prev = idx - 1

            if digits[idx] < 9:
                if digits[0] == 0:
                    return digits[1::]

            elif digits[idx] >= 10:
                digits[idx] = digits[idx] - 10
                digits[prev] += 1

            elif digits[idx] == 9:
                digits[idx] = 0
                digits[prev] += 1
            if digits[prev] == 9:
                if digits[0] == 0:
                    return digits[1::]

            idx -= 1

        if digits[0] == 0:
            return digits[1::]
        else:
            return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        [9, 8, 9]
        """
        for index in range(len(digits) - 1, -1, -1):
            digits[index] += 1
            if digits[index] != 10:
                return digits
            digits[index] = 0
        return [1] + digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one = 1
        i = 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0

            i += 1
        return digits[::-1]


solution = Solution()

if __name__ == "__main__":
    cases = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9],
        [9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9],
        [9, 8, 9],
        [9, 9],
        [8, 9, 9, 9],
        [9, 8, 9],
    ]
    for x in cases:
        print(solution.plusOne(x))
