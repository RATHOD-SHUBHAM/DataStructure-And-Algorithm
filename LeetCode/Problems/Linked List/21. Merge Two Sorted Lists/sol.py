# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tc: O(list1 + list2) | Sc: O(1)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        dummy = prev = ListNode(-1)
        
        if not p:
            return list2
        
        if not q:
            return list1
        
        while p and q:
            if p.val < q.val:
                prev.next = p
                p = p.next
                prev = prev.next
            else:
                prev.next = q
                q = q.next
                prev = prev.next 
        
        prev.next = p if p is not None else q
        
        return dummy.next