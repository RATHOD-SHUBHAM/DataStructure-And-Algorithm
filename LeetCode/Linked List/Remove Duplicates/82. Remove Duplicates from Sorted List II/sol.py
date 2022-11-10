'''

82. Remove Duplicates from Sorted List II

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




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# tc: O(n) | sc: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        
        dummy = ListNode(-1)
        dummy.next = head
        
        prev = dummy
        node = head
        
        while node and node.next:
            if node.val == node.next.val:
                
                while node and node.next and node.val == node.next.val:
                    node = node.next
                    
                child = node.next
                prev.next = child
                node.next = None
                node = child
            else:
                prev = node
                node = node.next
            
        return dummy.next