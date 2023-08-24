class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(common_prefix) != 0:
                common_prefix = common_prefix[:-1]
                if not common_prefix:
                    return ""
        return common_prefix
