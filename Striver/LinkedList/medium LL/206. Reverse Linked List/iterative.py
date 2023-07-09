# Tc: O(n) | Sc: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        nextNode = None
        curNode = head
        
        while curNode:
            nextNode = curNode.next
            
            # Change directions
            curNode.next = prevNode
            
            # Move the pointers
            prevNode = curNode
            curNode = nextNode
            
        if prevNode:
            head = prevNode
        
        return head