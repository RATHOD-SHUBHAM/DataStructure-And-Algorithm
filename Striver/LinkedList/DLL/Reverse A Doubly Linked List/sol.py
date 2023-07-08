class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        


def reverseDLL(head):
    # Write your code here
    curNode = head
    prevNode = None
    nextNode = None

    # Swap next and prev pointers
    while curNode:
        prevNode = curNode.prev
        nextNode = curNode.next

        curNode.next = prevNode
        curNode.prev = nextNode
        
        curNode = nextNode
        
    # Before changing head, check for the cases like
    # empty list and list with only one node
    if prevNode is not None:
        head = prevNode.prev
    
    return head