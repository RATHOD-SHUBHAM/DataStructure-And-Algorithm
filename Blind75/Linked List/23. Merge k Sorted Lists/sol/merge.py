# using merge sort + merge 2 sorted array logic

# time = O(nlogk) | space = O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedList = []
            
            # need to use 2 lists at once
            for i in range(0, len(lists) , 2):
                list1 = lists[i]
                # print("list1 : ",list1)
                
                list2 = lists[i+1] if (i + 1) < len(lists) else None
                # print("list2: ",list2)
                
                
                mergedList.append(self.mergeLL(list1 , list2))
                # print("mergedlist: ", mergedList)
                
            lists = mergedList
            
        return lists[0]
    
    def mergeLL(self , list1 , list2):
        p1 = list1
        p2 = list2
        prev = None
        
        if p1 is None: return p2
        if p2 is None: return p1
        
        while p1 and p2:
            if p1.val < p2.val:
                prev = p1
                p1 = p1.next
            else:
                if prev is not None:
                    prev.next = p2
                    
                prev = p2
                p2 = p2.next

                # Avoide Edge case: Make prev point to l1
                prev.next = p1
                
        if p1 is None:
            prev.next = p2
            
        return list1 if list1.val < list2.val else list2