# Remove node with the given key
# Tc: O(N) | Sc: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return
        
        curNode = head
        prevNode = None
        
        while curNode:
            if curNode.val == val:
                # if head
                if head.val == val:
                    head = head.next
                    curNode = head
                else:
                    prevNode.next = curNode.next
                    curNode.next = None
                    curNode = prevNode.next
            else:
                prevNode = curNode
                curNode = curNode.next
                
        return head