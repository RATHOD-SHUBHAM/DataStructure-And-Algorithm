# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        if a == 0:
            return abs(b)
        
        return self.gcd(b % a, a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = dummy = ListNode(-1)

        cur_node = head

        prev_node.next = cur_node

        # Check if there is only one node
        if not cur_node.next:
            return cur_node

        # Initial Setup
        prev_node = prev_node.next
        cur_node = cur_node.next

        while cur_node:
            a = prev_node.val
            b = cur_node.val

            x = self.gcd(a, b)

            new_node = ListNode(x)

            # Adjust Pointers
            prev_node.next = new_node
            new_node.next = cur_node

            # Move the Pointers
            prev_node = cur_node
            cur_node = cur_node.next
        
        return dummy.next

        