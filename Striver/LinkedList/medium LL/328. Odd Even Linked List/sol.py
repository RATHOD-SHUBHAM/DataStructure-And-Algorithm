# Tc: O(n) | Sc: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
            
        dummy1 = head
        dummy2 = head.next
        
        
        
        p1 = dummy1
        p2 = dummy2
        
        
        while p1:
            if p1.next.next:
                p1.next = p1.next.next
                p1 = p1.next
            
            if p2.next:
                p2.next = p2.next.next
                p2 = p2.next
                
            if (not p1.next) or (not p1.next.next):
                break
        
        p1.next = dummy2
        
        return dummy1