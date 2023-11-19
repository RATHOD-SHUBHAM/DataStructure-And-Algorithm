# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Time and Sc : O(l1 + l2)

class Solution:
    def lenLL(self, head):
        node = head
        Len = 0
        
        while node:
            Len += 1
            node = node.next
            
        return Len
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # get the len of linkedlist
        len_l1 = self.lenLL(l1)
        len_l2 = self.lenLL(l2)
        
        # step 1:sum the values without considering the carry
        p = l1
        q = l2
        summ = 0
        head = None
        
        while len_l1 > 0 and len_l2 > 0:
            if len_l1 >= len_l2:
                summ += p.val
                p = p.next
                len_l1 -= 1

            if len_l2 > len_l1:
                summ += q.val
                q = q.next
                len_l2 -= 1
                
            # create a new Node
            newNode = ListNode(summ)
            newNode.next = head
            head = newNode
            
            summ = 0
               
        # step 2: Extract the carry
        node = head
        carry = 0
        head = None
        
        while node or carry:
            val = carry # get the carry
            
            if node:
                if node.val > 9:
                    carry = 1
                    val += node.val - 10
                else:
                    carry = 0
                    val += node.val
                    
                    # if after adding the previous carry, my current number becomes greater than 9
                    if val > 9:
                        carry = 1
                        val = val - 10
                
            
            # create a new Node
            newNode = ListNode(val)
            newNode.next = head
            head = newNode
            
            
            # after iterating throught carry. My node is already at none. so dont need to move further again
            if node is None:
                break
                
            node = node.next
            
        return head