import itertools as it

inputs = [
    {"string": "abaxyzzyxf"},
    {"string": "a"},
    {"string": "it's highnoon"},
    {"string": "noon high it is"},
    {"string": "abccbait's highnoon"},
    {"string": "abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"},
    {"string": "abcdefgfedcba"},
    {"string": "abcdefghfedcbaa"},
    {"string": "abcdefggfedcba"},
    {"string": "zzzzzzz2345abbbba5432zzbbababa"},
    {"string": "z234a5abbbba54a32z"},
    {"string": "z234a5abbba54a32z"},
    {"string": "ab12365456321bb"},
    {"string": "aca"},
    {"string": "abaxyzzyxf"},
]


def longestPalindromicSubstring(string):
    pass


def longestPalindromicSubstring_slow(string):
    # abaxyzzyxf
    # xyzzyx
    if len(string) == 1:
        return string
    print(string)
    found_palindromes = []
    for idx in range(len(string) + 1):
        # if string == string[::-1]:

        for idx2 in range(len(string) + 1):
            if idx2 <= idx:
                continue
            if string[idx:idx2] == "xyzzyx":
                print("GOT HIMMMMMMM")
            if string[idx:idx2] == string[idx:idx2][::-1]:
                found_palindromes.append(string[idx:idx2])

    print(found_palindromes)
    print("return", max(found_palindromes, key=len))
    return max(found_palindromes, key=len)


if __name__ == "__main__":
    for test in inputs:

        print(longestPalindromicSubstring_slow(**test))
        print(longestPalindromicSubstring(**test))

        print(50 * "_")
