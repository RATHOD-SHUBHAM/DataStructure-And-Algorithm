# learn both recursive and iterative approach
# added notes

# Time = O(nlogn)
# space = O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        left = head
        # break the node in half
        right = self.getMid(head)
        
        # move the right pointer to next node and break the link at the division
        tmp = right.next
        right.next = None
        
        leftLL = self.sortList(left)
        rightLL = self.sortList(tmp)
        
        return self.mergeLL(leftLL, rightLL)
        
    def getMid(self, node):
        # tortise and hair method
        slow = node
        fast = node.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def mergeLL(self, l1, l2):
        cur = dummy = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        cur.next = l1 if l1 else l2
        
        return dummy.next