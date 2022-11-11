# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        newLL = dummy = ListNode(-1)
        
        p = l1
        q = l2
        carry = summ = 0
        
        while p or q or carry:
            summ += carry
            
            summ += 0 if p is None else p.val
            summ += 0 if q is None else q.val
            
            if summ > 9:
                carry = 1
                summ -= 10
            else:
                carry = 0
                
            newLL.next = ListNode(summ)
            newLL = newLL.next
            summ = 0
            
            if p is None and q is None:
                break
            elif p is None:
                q = q.next
            elif q is None:
                p = p.next
            else:
                p = p.next
                q = q.next
        
        return dummy.next