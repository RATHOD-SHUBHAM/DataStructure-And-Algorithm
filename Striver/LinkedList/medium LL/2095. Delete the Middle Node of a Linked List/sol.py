# Tc: O(N) | Sc: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return None
        
        # Get the middle Node
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        
        prev.next = slow.next
        del(slow)
        
        
        return head