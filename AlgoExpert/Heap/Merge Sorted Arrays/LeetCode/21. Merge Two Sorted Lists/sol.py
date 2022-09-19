# time = O(n + m)
# space = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = list1
        p2 = list2
        prev = None
        
        if not p1: return p2
        if not p2: return p1
        
        while p1 and p2:
            if p1.val < p2.val:
                prev = p1
                p1 = p1.next
            else:
                if prev is not None:
                    prev.next = p2
                prev = p2
                p2 = p2.next
                prev.next = p1
                
        if p1 is None:
            prev.next = p2
            
        return list1 if list1.val < list2.val else list2