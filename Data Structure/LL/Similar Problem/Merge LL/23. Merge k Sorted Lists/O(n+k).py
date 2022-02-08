# Time = O(nlogn) 
# space = O(n+k) where n=total number of nodes, k=number of lists

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
        
        # because ill copy my merge list into list. length of my lsit will keep reducing
        while len(lists) > 1:
            mergeList = []
            
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergeList.append(self.mergeTwoSortedList(list1,list2))
                
            # copy the mergeList to actual list
            lists = mergeList[:]
        
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