class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    prevNode = None
    curNode = head

    while curNode:
        if curNode.data == k:
            if curNode == head:
                head = head.next
                del(curNode)
                curNode = head
            elif curNode.next == None:
                nextNode = curNode.next
                prevNode.next = nextNode
                
                del(curNode)
                curNode = nextNode
            else:
                nextNode = curNode.next
                prevNode.next = nextNode
                nextNode.prev = prevNode

                del(curNode)
                curNode = nextNode
        else:
            prevNode = curNode
            curNode = curNode.next
    
    return head