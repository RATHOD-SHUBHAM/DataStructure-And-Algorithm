# Tc: O(nlogn) | Sc: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        # Get all the node value in list.
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        
        # print(nodes)

        # Sort the values
        nodes.sort()
        
        # Create a new linked list
        dummy = prev = ListNode()
        for node in nodes:
            prev.next = ListNode(node)
            prev = prev.next
        
        return dummy.next

