

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        for i, long in enumerate(s):
            if long.swapcase() not in s:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s1 if len(s1) >= len(s2) else s2
        
        return s