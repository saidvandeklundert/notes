from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        _max = 0
        for sentence in sentences:
            words = sentence.split(" ")
            if len(words) > _max:
                _max = len(words)
        return _max


alist = [
    ["alice and bob love leetcode", "i think so too", "this is great thanks very much"],
    ["please wait", "continue to fight", "continue to win"],
]
# 6, 3

for sentences in alist:
    print(Solution().mostWordsFound(sentences))
