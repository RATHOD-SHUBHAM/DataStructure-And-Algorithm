'''
Keep traversing till the shorter LL covers the gap/difference in the length 

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pt1 = headA
        pt2 = headB
        
        # move the pointer until one of then reach none
        while pt1 != pt2:
            if pt1 is None:
                # Cover the distance
                pt1 = headB
            else:
                pt1 = pt1.next
            
            if pt2 is None:
                # cover the distance
                pt2 = headA
            else:
                pt2 = pt2.next
        
        return pt1