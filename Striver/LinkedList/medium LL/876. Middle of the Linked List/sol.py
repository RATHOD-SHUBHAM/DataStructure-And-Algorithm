# Tc: O(n) | Sc: O(1)

# Definition for singly-linked list.
'''
1->2->3->4
op = 3
'''
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
    
# --------------------------------------------------------------------
# Definition for singly-linked list.
'''
1->2->3->4
op = 2
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortise = head
        heir = head.next
        
        while heir and heir.next:
            tortise = tortise.next
            heir = heir.next.next
        
        return tortise