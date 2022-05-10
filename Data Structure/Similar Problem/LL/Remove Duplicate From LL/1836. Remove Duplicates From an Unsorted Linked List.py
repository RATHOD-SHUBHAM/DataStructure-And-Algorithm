'''
1836. Remove Duplicates From an Unsorted Linked List
Medium


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

# Time and space = O(n)
# My sol: https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/discuss/1833696/Counter-or-python-3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # hold the count of each node
        count = self.countOccurance(head)
        # print(count)
        
        # create a sentinel node
        dummy = ListNode()
        prev_node = dummy
        prev_node.next = head
        
        cur_node = head
        
        while cur_node:
            # check if it has occured only once. If yes then just move the pointer
            if count[cur_node.val] == 1:
                prev_node = cur_node
                cur_node = cur_node.next
            else:
                # the node appeared more than once
                while cur_node and count[cur_node.val] != 1:
                    cur_node = cur_node.next
                
                prev_node.next = cur_node
                
        return dummy.next
        
        
    
    def countOccurance(self, head):
        dic = {}
        
        cur_node = head
        
        while cur_node:
            # initializing
            if cur_node.val not in dic:
                dic[cur_node.val] = 0
            
            dic[cur_node.val] += 1
            
            cur_node = cur_node.next
        
        # print(dic)
        return dic