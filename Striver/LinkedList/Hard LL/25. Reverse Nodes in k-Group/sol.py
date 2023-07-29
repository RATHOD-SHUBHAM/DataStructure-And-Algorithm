# class ListNode:
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        groupPrev = dummy
        
        while True:
            kth_node = self.get_K_node(groupPrev , k)
            
            if not kth_node:
                break
            
            groupNext = kth_node.next # the next node of group
            nextGroup_prevNode = groupPrev.next # keep track of the next group's previous node
            curNode = groupPrev.next
            
            # reverse the node
            prevNode = groupNext
            
            while curNode != groupNext:
                nextNode = curNode.next
                
                curNode.next = prevNode
                
                prevNode = curNode
                curNode = nextNode
            
            # adjust the end pointers of the group
            groupPrev.next = kth_node
            groupPrev = nextGroup_prevNode
        
        return dummy.next
    
    def get_K_node(self, curNode , K):
        while curNode and K > 0:
            curNode = curNode.next
            K -= 1
        
        return curNode