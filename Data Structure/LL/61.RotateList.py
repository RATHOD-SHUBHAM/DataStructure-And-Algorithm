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




'''
# 1. calculate len of LL. --> here Ill also get pointer to last node
# 2. Check when the rotation occur --> Calculate OffSet
# 3. if offset is 0. no rotation takes place
# When K is positive: 
    Need to remove element from back ie -- ( length of LL - Offset )
# when K is negative
    Need to remove elements from front
    
# 4. Traverse just before the position and change its pointer.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        lengthLL = 1
        curNode = head
        
        # base case
        if curNode is None:
            return head
        
        while curNode.next:
            curNode = curNode.next
            lengthLL += 1
            
        # calculate offset
        offset = abs(k) % lengthLL
        
        if offset == 0:
            return head
        
        # check the direction of rotation
        if k>0:
            pos = lengthLL - offset
        else:
            pos = offset
            
        right = head
            
        # got upto the pre position
        for _ in range(pos - 1):
            right = right.next
            
        curNode.next = head
        head = right.next
        right.next = None
        
        return head