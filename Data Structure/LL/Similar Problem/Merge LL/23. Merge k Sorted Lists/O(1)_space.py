# Time = O(nlogn) 
# space = O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case
        if len(lists) < 1:
            return 
        
        jump = 1
        
        while jump < len(lists):
            for i in range(0,len(lists) - jump, jump*2):
                print(i)
                lists[i] = self.mergeTwoSortedList(lists[i], lists[i+jump])
                print(lists[i])
            
            jump *= 2
        
        return lists[0] if len(lists) > 0 else None
        
    
    def mergeTwoSortedList(self, list1, list2):
        p1 = list1
        p2 = list2
        prev = None
        
        # base case
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        
        while p2 and p1:
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