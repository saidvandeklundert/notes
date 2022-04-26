from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end_idx = len(s) - 1
        start_idx = 0
        while start_idx < end_idx:
            s[start_idx], s[end_idx] = s[end_idx], s[start_idx]
            start_idx += 1
            end_idx -= 1
        print(s)


if __name__ == "__main__":
    alist = [["h", "e", "l", "l", "o"], ["H", "a", "n", "n", "a", "h"], ["k", "u", "t"]]
    for s in alist:
        print(Solution().reverseString(s))
