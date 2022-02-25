# Time = O(n^2)
# Space = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-math.inf) # or else bby default it will take 0
        # i cant make it None since dummy will be used for comparison
        dummy.next = head
        
        prevNode = dummy
        curNode = head
        
        while curNode:
            
            # if curNode is greater than prevNode then dont swap
            if curNode.val >= prevNode.val:
                prevNode = curNode
                curNode = curNode.next
                continue
            
                
            tempNode = dummy
            while tempNode.next and tempNode.next.val < curNode.val:
                tempNode = tempNode.next
                
            # reassigning the pointers
            prevNode.next = curNode.next
            curNode.next = tempNode.next
            tempNode.next = curNode
            
            curNode = prevNode.next
    
        return dummy.next