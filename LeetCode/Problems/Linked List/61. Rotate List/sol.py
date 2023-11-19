'''

61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tc: O(n) | Sc: O(1)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        
        lastNode = head
        Len = 1
        
        while lastNode.next:
            Len += 1
            lastNode = lastNode.next
        
        offset = k % Len
        
        if offset == 0:
            return head
        
        shiftPos = Len - offset if k > 0 else offset
        
        node = head
        
        for _ in range(shiftPos - 1):
            node = node.next
            
        lastNode.next = head
        head = node.next
        node.next = None
        
        return head