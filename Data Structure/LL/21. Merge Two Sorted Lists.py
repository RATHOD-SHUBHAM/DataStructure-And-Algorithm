'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2

        cur = head = ListNode(0)

        while p and q:
            if p.val < q.val:
                cur.next = ListNode(p.val)
                cur = cur.next
                p = p.next
            else:
                cur.next = ListNode(q.val)
                cur = cur.next
                q = q.next

        while p:
            cur.next = ListNode(p.val)
            cur = cur.next
            p = p.next

        while q:
            cur.next = ListNode(q.val)
            cur = cur.next
            q = q.next
	
        return head.next