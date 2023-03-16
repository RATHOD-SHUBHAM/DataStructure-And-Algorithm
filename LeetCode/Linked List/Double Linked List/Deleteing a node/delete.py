'''
# Deletign at 3 different position

1. Delete a Node
2. Delete all the nodes with particular value
3. delete a node at particular position
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # remove a particular node
    def removeNode(self,node):
        # check if it is head node
        if self.head == node:
            self.head = self.head.next

        # if tail node
        if self.tail == node:
            self.tail = self.tail.prev

        # if some other node
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None
        

    # remove all the node with particular value
    def removeNodeparticularvalue(self,value):
        curNode = self.head

        while curNode is not None:
            temp = curNode # if i remove the node directly I loose the pointers to move forward
            curNode = curNode.next

            if temp.val == value:
                self.removeNode(temp) 


    # remove node at particular position
    def removeparticularposition(self,k):
        curNode = self.head
        position = 0

        while curNode is not None:
            position += 1
            temp = curNode
            curNode = curNode.next

            if position == k:
                self.removeNode(temp)

    