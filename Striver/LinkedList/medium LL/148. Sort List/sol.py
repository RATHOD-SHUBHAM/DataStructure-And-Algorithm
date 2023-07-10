'''
Merge Sort:
    1. Divide the LL into individual nodes.
    2. Sort and Merge the nodes.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if (not head) or (not head.next):
            return head
        
        # break the LL into 2 half
        left = head
        right = self.getMid(head)
        
        tmp = right.next
        right.next = None
        
        # break the two LL even more
        left_LL = self.sortList(left)
        right_LL = self.sortList(tmp)
        
        # merge the node
        return self.mergeLL(left_LL , right_LL)
        
    # returns the middle node of LL
    def getMid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    # merge the two LL
    def mergeLL(self, L1, L2):
        cur = dummy = ListNode()
        
        while L1 and L2:
            if L1.val < L2.val:
                cur.next = L1
                L1 = L1.next
            else:
                cur.next = L2
                L2 = L2.next
            
            cur = cur.next
            
        # now attach the last node
        cur.next = L1 if L1 else L2
        
        return dummy.next
        