# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values_list = []
        current_node = head
        while current_node:
            values_list.append(current_node.val)
            current_node = current_node.next
        return values_list == values_list[::-1]
       