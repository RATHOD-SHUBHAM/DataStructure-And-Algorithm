'''
1836. Remove Duplicates From an Unsorted Linked List

Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.

Return the linked list after the deletions.

 

Example 1:


Input: head = [1,2,3,2]
Output: [1,3]
Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].
Example 2:


Input: head = [2,1,1,2]
Output: []
Explanation: 2 and 1 both appear twice. All the elements should be deleted.
Example 3:


Input: head = [3,2,2,1,3,2,4]
Output: [1,4]
Explanation: 3 appears twice and 2 appears three times. After deleting all 3's and 2's, we are left with [1,4].
 

Constraints:

The number of nodes in the list is in the range [1, 105]
1 <= Node.val <= 105


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Tc: O(n) | Sc: O(n)
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        
        hashmap = {}
        node = head
        
        # add the value in hashmap . this helps to check if the value has duplicate or not
        while node:
            if node.val not in hashmap:
                hashmap[node.val] = 1 # if its there first time - val is 1
            else:
                hashmap[node.val] = 2 # if its present more than once - val is 2
            node = node.next
            
            
        # loop across and del duplicate node by checking the hashmap
        # accessing dictionay is O(1)
        prev = dummy
        node = head
        
        while node:
            # if there are duplicates then remove node
            if hashmap[node.val] == 2:
                child = node.next
                prev.next = child
                node.next = None
                node = child
            
            # if there are no duplicates - just move pointers 
            elif hashmap[node.val] == 1:
                prev = node
                node = node.next
            
        return dummy.next
                