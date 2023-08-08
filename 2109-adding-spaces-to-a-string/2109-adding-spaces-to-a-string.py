class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_parts = []
        start_index = 0
        for space in spaces:
            new_parts.append(s[start_index:space])
            new_parts.append(' ')
            start_index = space
        new_parts.append(s[start_index:])
        return ''.join(new_parts)
