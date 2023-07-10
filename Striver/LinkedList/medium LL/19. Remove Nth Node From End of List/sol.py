'''
Create a window of size n
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1) # sentinal node
        dummy.next = head
        
        left = dummy
        right = dummy
        
        # move the right pointer to window size of n
        for _ in range(n):
            right = right.next
            
        # check for single node
        if right == None:
            return None
        
        while right.next:
            left = left.next
            right = right.next
        
        next_node = left.next
        left.next = next_node.next
        del(next_node)
        
        return dummy.next