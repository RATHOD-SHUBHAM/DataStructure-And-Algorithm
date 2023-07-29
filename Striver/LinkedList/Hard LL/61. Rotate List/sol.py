# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # step1: et the len of LL
        endNode = head
        len_LL = 1
        
        while endNode.next:
            len_LL += 1
            endNode = endNode.next
        
        # print(endNode.val)
        # print(len_LL)
        
        # step2: mark the new start node
        startNode = head
        prev = None
        curNode = head
        
        # step3: Calculate the K value
        k = k % len_LL
        # print(k)
        
        # if there is no change that needs to be done
        if k == 0:
            return head
        
        diff = len_LL - k
        
        while diff > 0:
            prev = curNode
            curNode = curNode.next
            diff -= 1
        
        # print(curNode.val)
        # print(prev.val)
        
        # step4: break the node at end
        prev.next = None
        
        # step5: make curNode as head
        head = curNode
        
        # step6: attach the endNode to startNode
        endNode.next = startNode
        
        
        return head
        