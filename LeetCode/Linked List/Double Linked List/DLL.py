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
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head,node)

    def setTail(self, node):
        # Write your code here.
        if self.tail == None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail,node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        # check if the node to insert is a head or a tail
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
		
		# check if the node to insert already exist
        self.remove(nodeToInsert)
        
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
            
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
            
        self.remove(nodeToInsert)
        
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
            
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return
            
        curNode = self.head
        k = 1
        
        while curNode != None and k != position:
            curNode = curNode.next
            k += 1
        
        if k == position:
            self.insertBefore(curNode,nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        curNode = self.head
        
        while curNode is not None:
			# we cant just remove a node. because we will loose the pointer to next element.
			# because of that then we cant iterate
            temp = curNode
            curNode = curNode.next
            
            if temp.value == value:
                self.remove(temp)

    def remove(self, node):
        # remove head
        if node == self.head:
            self.head = self.head.next
			# return
		
		# remove tail
        if node == self.tail:
            self.tail = self.tail.prev
			# return
		
		# if other nodes
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
            
        node.prev = None
        node.next = None

	# return a particular node with that value
    def containsNodeWithValue(self, value):
        # Write your code here.
        curNode = self.head
        
        while curNode is not None and curNode.value != value:
            curNode = curNode.next
            
        return curNode is not None

    # iterate through dll
    def printdll(self):
        curNode = self.head
        while curNode:
            print(curNode.value)
            curNode = curNode.next

if __name__ == '__main__':
    # Test your code here,
    dll = DoublyLinkedList()

    one = Node(1)
    two = Node(2)
    three = Node(3)
    three2 = Node(3)
    three3 = Node(3)
    four = Node(4)
    five = Node(5)
    seven = Node(7)

    dll.setHead(one)
    dll.insertAfter(one, two)
    dll.insertAfter(two, three)
    dll.insertAfter(three,three2)
    dll.insertAfter(three2,three3)
    dll.insertAfter(three, four)
    dll.insertAfter(four, five)
    dll.insertAfter(five, seven)

    dll.printdll()
    print("\n")

    six = Node(6)
    dll.insertBefore(seven, six)

    dll.printdll()

    print("\n")
    
    dll.remove(three2)

    dll.printdll()
    print("\n")

    dll.removeNodesWithValue(3)

    dll.printdll()
    print("\n")

    dll.containsNodeWithValue(3)

    dll.printdll()
    print("\n")
