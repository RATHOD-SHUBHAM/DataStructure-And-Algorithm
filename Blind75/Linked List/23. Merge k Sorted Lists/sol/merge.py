# using merge sort + merge 2 sorted array logic

# time = O(nlogk) | space = O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        
        while len(lists) > 1:
            
            mergedLists = []

            for i in range(0, len(lists) , 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                
                mergedLists.append(self.mergeSort(list1, list2))
            
            lists = mergedLists
        
        return lists[0]
    
    def mergeSort(self, list1, list2):
        l1 = list1
        l2 = list2

        if not l1: return l2
        if not l2: return l1

        dummy = node = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            
            else:
                node.next = l2
                l2 = l2.next
            
            node = node.next

        if not l1:
            node.next = l2
        if not l2:
            node.next = l1
        
        return dummy.next