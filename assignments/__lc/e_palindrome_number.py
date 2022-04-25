class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_as_str = str(x)
        if "-" in num_as_str:
            return False
        if num_as_str == num_as_str[::-1]:
            return True
        return False


if __name__ == "__main__":
    alist = [121, -121, 10]
    for x in alist:
        print(Solution().isPalindrome(x))
