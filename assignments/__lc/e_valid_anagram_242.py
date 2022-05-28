import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        available = {}

        for char in s:
            if char in available:
                available[char] += 1
            else:
                available[char] = 1

        for char in t:
            if available.get(char) == 0:
                return False
            elif char not in available:
                return False
            available[char] -= 1

        res = list(available.values())
        res = [x for x in res if x != 0]
        if res:
            return False
        else:
            return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for x in s:
            tracker[x] += 1
        for x in t:
            tracker[x] -= 1
        return all(x == 0 for x in tracker.values())


alist = [["anagram", "nagaram"], ["rat", "car"], ["ab", "a"]]

for arg in alist:
    print(Solution().isAnagram(arg[0], arg[1]))
