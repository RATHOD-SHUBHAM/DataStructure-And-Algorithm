# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        prev = None
        
        if not l1 and not l2: 
            return
        
        if l1 and not l2:
            return l1
        
        if l2 and not l1:
            return l2
        
        while l1 and l2:
            if l1.val < l2.val:
                prev = l1
                l1 = l1.next
            else:
                if prev is not None:
                    prev.next = l2
                prev = l2
                l2 = l2.next
                prev.next = l1
                
        if l1 is None:
            prev.next = l2
            
        return list1 if list1.val < list2.val else list2