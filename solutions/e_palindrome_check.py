import ipdb

tests = ["abcdcba", "", "ba", "abcdefghihgfedcba", "abcdefghhgfedcba"]


def isPalindrome(string):
    reverse = string[::-1]
    if reverse == string:
        return True
    else:
        return False


def isPalindrome_rec(string):
    f = 0
    l = len(string) - 1
    if l < 0:
        return False
    return recursion(string, f, l)


def recursion(string, f, l):

    if f == l or f > l:
        return True
    if string[f] != string[l]:
        return False

    return recursion(string, f + 1, l - 1)


def isPalindrome_rec_sec(string, i=0):
    j = len(string) - 1 - i
    return (
        True
        if i >= j
        else string[i] == string[j] and isPalindrome_rec_sec(string, i + 1)
    )


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(isPalindrome(test))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(isPalindrome_rec(test))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(isPalindrome_rec_sec(test))
