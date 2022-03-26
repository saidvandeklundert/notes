class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_d_ransom = {}
        for char in ransomNote:
            if char in char_d_ransom:
                char_d_ransom[char] += 1
            else:
                char_d_ransom[char] = 1
        char_d_mag = {}
        for char in magazine:
            if char in char_d_mag:
                char_d_mag[char] += 1
            else:
                char_d_mag[char] = 1

        for char, occurence in ransomNote.items():
            if char_d_mag.get(char) is None:
                return False

            elif char_d_mag[char] < occurence:
                return False
        return True
