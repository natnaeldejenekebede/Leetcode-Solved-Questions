class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealths = list(map(sum, accounts))
        return max(wealths)
