# Creating new Linked List ----------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        
        # Grab the values from Linked List
        list_val = []

        for lst in lists:
            # print(lst)
            while lst:
                list_val.append(lst.val)
                lst = lst.next
        
        # Sort the list
        list_val.sort()

        # Create a new Linked List
        dummy = node = ListNode()
        for i in range(len(list_val)):
            curNode = ListNode(list_val[i])
            node.next = curNode
            
            curNode = curNode.next
            node = node.next
        
        return dummy.next
    

# Merge Sort ----------------------------------------------------------------------


# Merge Sort + Merge 2 sorted array (lc: 21)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Merge Sort
        while len(lists) > 1:
            
            mergedList = []

            # use 2 lists at once
            for i in range(0, len(lists), 2):

                list1 = lists[i]
                
                list2 = lists[i+1] if (i+1) < len(lists) else None

                mergedList.append(self.mergeSorted(list1, list2))
                # print(mergedList)

            lists = mergedList
        
        # print(lists)
            
        return lists[0]


    # Merge 2 Sorted array
    def mergeSorted(self, list1, list2):

        l1 = list1
        l2 = list2

        if not l1: return l2
        if not l2: return l1

        dummy = prev = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            
            prev = prev.next
        
        if not l1:
            prev.next = l2
        if not l2:
            prev.next = l1
        
        return dummy.next