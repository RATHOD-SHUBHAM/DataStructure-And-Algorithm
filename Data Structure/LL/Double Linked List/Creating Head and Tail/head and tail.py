class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head,node)

    def setTail(self,node):
        if self.head == None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail,node)