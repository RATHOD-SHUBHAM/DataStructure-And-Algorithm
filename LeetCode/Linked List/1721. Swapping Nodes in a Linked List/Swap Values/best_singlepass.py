# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Tc: O(n) | Sc: O(1)

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        frontNode = head
        node = head
        ll_len = 0
        
        
        while node:
            ll_len += 1
            
            # getting the front node value
            if ll_len == k:
                frontNode = node
                endNode = head # starting the end node - as endNode is K popsition behind lastNode of linked List
                
            if ll_len > k:
                endNode = endNode.next
            
            node = node.next

            
        frontNode.val , endNode.val = endNode.val , frontNode.val
        
        return head