# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle point of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        # Step 3: Merge the two halves of the linked list
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
