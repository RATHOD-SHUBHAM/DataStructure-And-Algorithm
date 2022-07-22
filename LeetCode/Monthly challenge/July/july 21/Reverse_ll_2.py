'''
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


'''

'''
4 step process:
1. Locating the start point.
2. Place pointers to identify the start
3. Reverse the node in btn
4. Connect the start and end


Tc: O(n)
Sc: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        cur = head
        
        # step 1
        while left > 1:
            prev = cur
            cur = cur.next
            left -= 1
            right -= 1 # calculating the remaining distance
            
        #step 2:
        con = prev 
        tail = cur
        
        # step 3:
        while right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            right -= 1
            
        #step 4:
        if con:
            con.next = prev
        # if we started from first position
        else:
            head = prev
        
        tail.next = cur
        
        return head
        