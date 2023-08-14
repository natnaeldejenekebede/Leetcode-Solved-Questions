class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sorted_p = sorted(p)
        anagram_indices = []
        
        for i in range(len(s) - len(p) + 1):
            if sorted(s[i:i+len(p)]) == sorted_p:
                anagram_indices.append(i)
        
        return anagram_indices
