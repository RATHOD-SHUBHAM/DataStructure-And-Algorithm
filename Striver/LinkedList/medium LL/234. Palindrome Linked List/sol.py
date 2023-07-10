# Tc: O(n) | Sc: O(1)

'''
# Steps: 
    1. Get the middle node of the linkedList.
    2. Reverse the second half of the linkedList.
    3. Compare both the linkedList.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Get the middle node of the LL
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # print(slow.val)
        
        # Step 2: Reverse the LL
        prevNode = None
        curNode = slow
        nextNode = None
        
        while curNode:
            nextNode = curNode.next
            
            # change the pointer
            curNode.next = prevNode
            
            # change the ponter
            prevNode = curNode
            curNode = nextNode
        
        if prevNode:
            p2 = prevNode
        
        # print(p2.val)
        
        # step 3: Compare 2 LL
        p1 = head
        
        while p1 != slow:
            if p1.val != p2.val:
                return False
            
            p1 = p1.next
            p2 = p2.next
        
        return True