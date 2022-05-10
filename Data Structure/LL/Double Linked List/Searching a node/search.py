class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, Node):
        if self.head is None:
            self.head = Node
            self.tail = Node
        else:
            self.insertBefore(self.head,Node)

    def setTail(self,Node):
        if self.tail == None:
            self.setHead(Node)
        else:
            self.insertAfter(self.tail,Node)
        
    def searchNode(self,k):
        # serach for node with value k
        curNode = self.head

        while curNode is not None and curNode.val != k:
            curNode = curNode.next

        return None if curNode == None else curNode.value