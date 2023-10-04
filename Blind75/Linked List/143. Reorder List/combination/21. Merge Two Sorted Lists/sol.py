# Tc : O(m + n) | Sc: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            
            prev = prev.next
        
        if not l1:
            prev.next = l2
        elif not l2:
            prev.next = l1
        
        return dummy.next

        