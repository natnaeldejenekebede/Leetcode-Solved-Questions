class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_count = [0] * 26
        t_char_count = [0] * 26

        for char in s:
            s_char_count[ord(char) - ord('a')] += 1

        for char in t:
            t_char_count[ord(char) - ord('a')] += 1

        return s_char_count == t_char_count
