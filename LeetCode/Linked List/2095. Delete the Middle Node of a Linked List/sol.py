# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# tc: O(n) | Sc: O(1)

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return 
        
        left = head
        right = head.next.next
        
        while right and right.next:
            left = left.next
            right = right.next.next
            
        left.next = left.next.next
        
        return head