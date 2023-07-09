# Tc: O(n) | Sc: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortise = head
        heir = head
        
        while heir and heir.next:
            tortise = tortise.next
            heir = heir.next.next
        
        return tortise