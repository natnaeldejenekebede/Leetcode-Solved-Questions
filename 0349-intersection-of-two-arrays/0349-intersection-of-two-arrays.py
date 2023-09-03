class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)
        return list(unique_nums1.intersection(unique_nums2))
