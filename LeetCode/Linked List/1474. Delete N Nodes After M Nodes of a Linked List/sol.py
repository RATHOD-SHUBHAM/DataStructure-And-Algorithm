# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# tc: O(n) | O(1)

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        node = head
        
        # O(n)
        while node:
            for _ in range(m - 1):
                if node.next:
                    node = node.next
                else:
                    break
                    
            if node.next:
                delNode = node.next
            else:
                break
            
            for _ in range(n):
                if delNode.next is not None:
                    delNode = delNode.next
                else:
                    delNode = None
                    break
                    
            node.next = delNode
            node = delNode
            
        return head
            