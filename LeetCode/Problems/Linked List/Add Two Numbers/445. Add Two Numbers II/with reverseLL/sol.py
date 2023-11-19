# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tc : O(n + m) | Sc: O(n+m)

class Solution:
    def reverseLL(self, head):
        node = head
        prev = None
        
        while node:
            child = node.next
            
            node.next = prev
            prev = node
            node = child
        
        return prev
    
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        reverse_l1 = self.reverseLL(l1)
        reverse_l2 = self.reverseLL(l2)
        
        dummy = newLL = ListNode(-1)
        
        p = reverse_l1
        q = reverse_l2
        
        carry = 0
        
        while p or q or carry:
            summ = carry
            
            summ += 0 if p is None else p.val
            summ += 0 if q is None else q.val
            
            if summ > 9:
                summ -= 10
                carry = 1
            else:
                carry = 0
                
            
            newLL.next = ListNode(summ)
            newLL = newLL.next
            
            if p is None and q is None:
                continue
            elif p is None:
                q = q.next
            elif q is None:
                p = p.next
            else:
                p = p.next
                q = q.next
                
                
        twoNum = self.reverseLL(dummy.next) 
        
        return twoNum
        