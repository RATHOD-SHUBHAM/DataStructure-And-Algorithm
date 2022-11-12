# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        node = head
        prev = None
        
        while node:
            child = node.next
            
            node.next = prev
            
            prev = node
            node = child
            
        return prev
    
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        reverseLL = self.reverse(slow.next)
        
        slow.next = None
        
        p1 = head
        p2 = reverseLL
        
        while p2:
            p3 = p1.next
            p4 = p2.next
            
            p1.next = p2
            p2.next = p3
            
            p1 = p3
            p2 = p4
            
        return head