# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Tc: O(n) | Sc: O(1)

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        frontNode = endNode = head
        
        # first pass get the len of linkedList
        node = head
        ll_len = 0
        while node:
            ll_len += 1
            
            # getting the front node value
            if ll_len == k:
                frontNode = node
            
            node = node.next
            
        # move to end node
        end_k = ll_len - k
        for _ in range(end_k):
            endNode = endNode.next
            
            
        frontNode.val , endNode.val = endNode.val , frontNode.val
        
        return head