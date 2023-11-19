'''

82. Remove Duplicates from Sorted List II
Medium


Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

'''

# Time = O(n)
# Space = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        prev_node = dummy
        prev_node.next = head
        
        cur_node = head
        
        while cur_node:
            next_node = cur_node.next
            
            if next_node is None:
                break
            
            if cur_node.val != next_node.val:
                prev_node = cur_node
                cur_node = next_node
            else:
                while next_node and next_node.val == cur_node.val:
                    next_node = next_node.next
                    
                cur_node = next_node
                prev_node.next = cur_node
                
        return dummy.next