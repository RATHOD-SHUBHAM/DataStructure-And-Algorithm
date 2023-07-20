'''
1. Calculate length of list A and length of list B.
2. Set the start pointer for the longer list.
3. Step the pointers through the list together.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Step1: get the length of 2 LL
        # LL - 1
        M = 0
        pt1 = headA
        
        while pt1:
            M += 1
            pt1 = pt1.next
        
        # LL - 2    
        N = 0
        pt2 = headB
        
        while pt2:
            N += 1
            pt2 = pt2.next
        
        # print(M , N)
        
        # Step2: Assign pointers
        diff = 0
        
        if M < N:
            pt1 = headA
            diff = N - M
            
            pt2 = headB
            while diff != 0:
                pt2 = pt2.next
                diff -= 1
                
        elif N < M:
            pt2 = headB
            diff = M - N
            
            pt1 = headA
            while diff != 0:
                pt1 = pt1.next
                diff -= 1
                
        else:
            pt1 = headA
            pt2 = headB
        
        # print(diff)
        # print(pt1.val)
        # print(pt2.val)
        
        # Step 3: move the pointer together
        
        while pt1 and pt2 :
            
            if pt1 == pt2:
                return pt1
            
            pt1 = pt1.next
            pt2 = pt2.next
        
        return None