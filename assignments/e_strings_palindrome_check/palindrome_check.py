import rust

inputs = [
    {"string": "abcdcba"},
    {"string": "a"},
    {"string": "ab"},
    {"string": "aba"},
    {"string": "abb"},
    {"string": "abba"},
    {"string": "abcdefghhgfedcba"},
    {"string": "abcdefghihgfedcba"},
    {"string": "abcdefghihgfeddcba"},
]
"""
Palindrome is a string that is written the same way forwards and backwards.

Write a function that returns a bool based on if the string is a palindrome.
"""
# O(n2) time, O(1)? space
def isPalindromeSlow(string):
    if string == string[::-1]:
        return True
    return False


# O(n) time, O? space
def isPalindrome_recursion(string):
    # print("start", string)
    # print("main", id(string))
    if len(string) == 1:
        return True
    elif string[0] == string[-1]:
        return helper(string[1:-1])
    return False


def helper(string):
    # print("helper", string)
    # print("helper", id(string))
    if len(string) == 1:
        return True
    elif len(string) == 2:
        if string[0] == string[1]:
            return True
        else:
            return False
    elif string[0] == string[-1]:
        return helper(string[1:-1])
    return False


# O(n) time, O(1) space
def isPalindrome(string):
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


if __name__ == "__main__":
    for test in inputs:
        print(isPalindromeSlow(**test))
        print(isPalindrome_recursion(**test))
        print(isPalindrome(**test))
        print(rust.is_palindrome_slow(**test))
