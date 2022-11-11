# Floyd's Cycle Finding Algorithm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next:
            return head
        
        slow = head
        fast = head.next
        
        while slow != fast:
            
            if not fast or not fast.next.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
        return True
        