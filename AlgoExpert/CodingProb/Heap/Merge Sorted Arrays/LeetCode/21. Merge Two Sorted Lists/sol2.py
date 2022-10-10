# time = O(n + m)
# space = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        p = list1
        q = list2
        prev = dummy = ListNode(-1)
        
        while p and q:
            if p.val <= q.val:
                prev.next = p
                p = p.next
                prev = prev.next
            else:
                prev.next = q
                q = q.next
                prev = prev.next
                
        prev.next = q if q is not None else p
        
        return dummy.next