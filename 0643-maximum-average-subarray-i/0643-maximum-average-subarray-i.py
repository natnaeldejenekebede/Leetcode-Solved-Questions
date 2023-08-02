class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix_sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        max_avg = float('-inf')
        for i in range(k, len(nums) + 1):
            max_avg = max(max_avg, prefix_sums[i] - prefix_sums[i - k])

        return max_avg / k
