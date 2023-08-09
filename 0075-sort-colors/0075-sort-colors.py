class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_pointer, right_pointer = 0, len(nums) - 1
        current_index = 0
        
        while current_index <= right_pointer:
            if nums[current_index] == 0:
                nums[current_index], nums[left_pointer] = nums[left_pointer], nums[current_index]
                left_pointer += 1
                current_index += 1
            elif nums[current_index] == 2:
                nums[current_index], nums[right_pointer] = nums[right_pointer], nums[current_index]
                right_pointer -= 1
            else:
                current_index += 1
