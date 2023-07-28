class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    curNode = head

    while curNode:
        nextNode = curNode.next

        if nextNode and curNode.data == nextNode.data:
            NN_node = nextNode.next

            if NN_node:
                curNode.next = NN_node
                NN_node.prev = curNode

                del(nextNode)
                nextNode = NN_node
            else:
                curNode.next = None
                del(nextNode)
        
        elif not nextNode:
            break

        else:
            curNode = nextNode
    
    return head

