class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]  # Create a copy of nums1 with valid elements
        i = j = 0  # Pointers for nums1 and nums2
        
        for k in range(m + n):
            if i < m and (j >= n or temp[i] <= nums2[j]):
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
