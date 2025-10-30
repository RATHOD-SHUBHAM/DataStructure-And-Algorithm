# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head # last node - keep track of last node as this will be new head

        if head.next:
            # get the last node
            newHead = self.reverseList(head.next)

            # Change pointers for current node
            head.next.next = head
            head.next = None

        # we will return last node as new head
        return newHead