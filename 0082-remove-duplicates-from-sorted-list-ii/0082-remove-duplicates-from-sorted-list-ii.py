# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, current_node: Optional[ListNode]) -> Optional[ListNode]:
        if not current_node or not current_node.next:
            return current_node
        
        if current_node.val == current_node.next.val:
            while current_node.next and current_node.val == current_node.next.val:
                current_node = current_node.next
            return self.deleteDuplicates(current_node.next)
        else:
            current_node.next = self.deleteDuplicates(current_node.next)
            return current_node

