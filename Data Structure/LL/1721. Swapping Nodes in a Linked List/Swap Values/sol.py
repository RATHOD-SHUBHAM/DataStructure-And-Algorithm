'''

1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100


'''

# Make pointer p1 move K value ahead of p2
# So when p1 reaches the end ,p2 will be at n-k node


# Time = O(n)
# Space = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = p2 = head
        
        # because p1 is already on head node. start index from 1
        for i in range(1, k):
            p1 = p1.next
            
        curNode = p1
        curNode = p1.next
        
        while curNode:
            curNode = curNode.next
            p2 = p2.next
            
        p1.val , p2.val = p2.val , p1.val
        
        return head