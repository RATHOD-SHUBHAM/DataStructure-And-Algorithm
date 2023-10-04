# Tc: O(n) | Sc: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = None
        cur = head

        while cur:
            # keeping track of next node
            nextNode = cur.next

            # reversing the pointer
            cur.next = prev
            
            # re-assigning the values
            prev = cur
            cur = nextNode
        
        return prev
