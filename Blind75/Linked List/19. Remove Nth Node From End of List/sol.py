# Tc: O(n) | Sc: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None

        dummy = ListNode(-1)
        dummy.next = head

        navNode = curNode = dummy

        # Create a distance of n - nodes
        for _ in range(n):
            navNode = navNode.next
        
        while navNode:
            navNode = navNode.next

            prev = curNode
            curNode = curNode.next
        
        # Delete the nth node from back
        prev.next = curNode.next
        del(curNode)

        return dummy.next
        