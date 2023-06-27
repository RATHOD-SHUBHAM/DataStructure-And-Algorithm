
class node:
    def __init__(self):
        self.data = None
        self.next = None


def delNode(head, k):
    # Code here
    curNode = head
    prevNode = None
    
    if k == 1:
        head = head.next
        return head
    
    curPos = 1
    
    while curNode != None and curPos < k:
        prevNode = curNode
        curNode = curNode.next
        curPos += 1
        
    # curNode == None
    if curPos < k:
        return
    
    prevNode.next = curNode.next
    curNode.next = None
    del(curNode)
    
    return head