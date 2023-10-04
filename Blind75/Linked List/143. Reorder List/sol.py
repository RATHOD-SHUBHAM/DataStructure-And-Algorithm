# TC: O(n) | Sc: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # base case
        if head is None:
            return head
        
        # breaking the linked list into two
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        # reversing the Linked List
        reversedLL = self.reversed(slow.next)
        
        slow.next = None
        
        
        # combining the linked list
        p1 = head
        p2 = reversedLL
        
        while p1 and p2:
            p3 = p1.next
            p4 = p2.next
            
            p1.next = p2
            p2.next = p3
            
            p1 = p3
            p2 = p4
            
        return head
            
        
        
    def reversed(self,node):
        prev = None
        cur = node
        
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev