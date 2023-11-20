# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next

        while slow != fast:
            # if there is None at end, then there cant be any cycle
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next
        
        return True