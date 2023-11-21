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