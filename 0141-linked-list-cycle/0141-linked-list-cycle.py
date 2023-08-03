# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        marker_node = ListNode(None)
        current_node = head
        
        while current_node:
            if current_node.next is marker_node:
                return True
            next_node = current_node.next
            current_node.next = marker_node
            current_node = next_node
        
        return False


        