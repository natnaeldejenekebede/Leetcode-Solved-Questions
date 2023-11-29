class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_count = 0
        while n:
            n &= (n - 1)
            binary_count += 1
        return binary_count


