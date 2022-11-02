# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
    # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
            # return
        else:
            # insert before the current head
            self.insertBefore(self.head,node)

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:  # initially both head and tail points to a single node
            # self.head = node
            # self.tail = node
            self.setHead(node)
        else:
            self.insertAfter(self.tail,node)

    # basically this is update
    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        
        # suppose we want to insert first element of ll form this function
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        
        # remove from that postion adn update at a differnt place
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        
        # if we are inserting at position one then it is head
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
            
        

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert==self.tail:
            return
        
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        
        # if we are inserting in end . then it is tail
        if node.next is None:
            self.tail = nodeToInsert # tail already has connections, just make last node as tail
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
        

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return
        
        node = self.head
        currentPosition = 1
        
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
            
        if node is not None:	
            self.insertBefore(node,nodeToInsert)
        else:
            self.setTail(nodeToInsert)
        

    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
        
        while node is not None:
            duplicateNode = node
            node = node.next # after removing the node i need to further traverse
            
            if duplicateNode.value == value:
                self.remove(duplicateNode)
            

    def remove(self, node):
        # Write your code here.
        # remove head node
        if node == self.head:
            self.head = self.head.next
        
        # remove the tail  node
        if node == self.tail:
            self.tail = self.tail.prev
            
        # other node
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        # after removing the connection of the node make them point to None	
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None and node.value != value:
            node = node.next
            
            
        # when we break out of the loop two things happens
        # 1. either the node is NONE
        # 2. The value is present
        # return true when node is Not None	
        return node is not None
			
		
