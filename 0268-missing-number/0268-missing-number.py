class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for index, num in enumerate(nums):
            result ^= index ^ num
        return result
