# Time and space = O(n + m)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        
        # base case
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        
        if p1.val < p2.val:
            p1.next = self.mergeTwoLists(p1.next,p2)
            return p1
        else:
            p2.next = self.mergeTwoLists(p2.next,p1)
            return p2