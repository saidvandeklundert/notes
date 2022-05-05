class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for start in range(len(s) - 1):

            current_str = ""
            for char in s[start::]:

                if char not in current_str:
                    current_str += char

                elif char in current_str:

                    if len(current_str) > longest:
                        longest = len(current_str)
                        current_str = ""
                    break

        return longest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        mx = left = 0
        for right, c in enumerate(s):
            if c in seen:
                left = max(left, seen[c] + 1)
            seen[c] = right
            mx = max(mx, right - left + 1)
        return mx


alist = ["abcabcbb", "bbbbb", "pwwkew"]
# 3
# 1
# 3

for string in alist:
    print(Solution().lengthOfLongestSubstring(string))
