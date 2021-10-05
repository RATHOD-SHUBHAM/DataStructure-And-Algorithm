# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        # creating my own linked List
        myNode = head = ListNode(0)

        carry = 0
        while node1 or node2 or carry:
            curr_val = carry

            curr_val += 0 if node1 is None else node1.val
            curr_val += 0 if node2 is None else node2.val

            if curr_val >= 10:
                curr_val -= 10
                carry = 1
            # you need the else part cause once the carry flag is set to zero ands again the next calculation if no carry is prodcued then carry flag must be set to zero
            else:
                carry = 0

            myNode.next = ListNode(curr_val)
            myNode = myNode.next

            if node1 is None and node2 is None:
                break
            elif node1 is None:
                node2 = node2.next
            elif node2 is None:
                node1 = node1.next
            else:
                node1 = node1.next
                node2 = node2.next

        return head.next
