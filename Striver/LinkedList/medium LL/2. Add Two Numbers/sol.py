# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = new_LL = ListNode(-1)
        
        p1 = l1
        p2 = l2
        
        carry = 0
        
        while p1 or p2 or carry:
            cur_sum = carry
            
            cur_sum += p1.val if p1 else 0
            cur_sum += p2.val if p2 else 0
            
            if cur_sum > 9:
                cur_sum -= 10
                carry = 1
            else:
                carry = 0
            
            new_LL.next = ListNode(cur_sum)
            new_LL = new_LL.next
            
            if p1 and p2:
                p1 = p1.next
                p2 = p2.next
            elif p1:
                p1 = p1.next
            elif p2:
                p2 = p2.next
            else:
                continue
        
        return dummy.next
        