# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = left = right = ListNode(-1)
        dummy.next = head

        # move the right pointer by n position
        while n > 0:
            right = right.next
            n -= 1
        
        # move both pointer at same pace
        while right.next:
            right = right.next
            left = left.next

        # Grab the node
        nxtNode = left.next.next

        # delete node
        left.next.next = None
        left.next = None

        # link the node
        left.next = nxtNode

        return dummy.next