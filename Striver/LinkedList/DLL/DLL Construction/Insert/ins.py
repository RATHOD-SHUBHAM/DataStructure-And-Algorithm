class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self) -> None:
        self.head = None

    def front(self, n):
        new_node = Node(n)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        
        self.head = new_node

    def end(self, n):
        new_node = Node(n)

        if self.head == None :
            self.head = new_node
            return
        

        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode

        new_node.prev = lastNode
        lastNode.next = new_node

    def after(self, node, n):
        if self.head == None or node == None:
            return
        
        new_node = Node(n)

        if node.next is not None:
            node.next.prev = new_node
        
        new_node.next = node.next

        new_node.prev = node
        node.next = new_node

    def before(self, node, n):
        if self.head == None or node == None:
            return
        
        new_node = Node(n)

        if node.prev is not None:
            node.prev.next = new_node
        
        new_node.prev = node.prev
        new_node.next = node

        node.prev = new_node

        if new_node.prev == None:
            self.head = new_node

    def insertAtPosition(self, position, nodeToInsert):

        if self.head == None:
            return


        if position == 1:
            nodeToInsert.next = self.head
            self.head.prev = nodeToInsert

            self.head = nodeToInsert

            return

        curPos = 0
        node = self.head
        prev_node = None
        
        
        while node and curPos < position - 1:
            prev_node = Node
            node = node.next

        if node == None:
            # set tail - end node
            nodeToInsert.prev = prev_node
            prev_node.next = nodeToInsert
            return
        else:
            if node.prev is not None:
                node.prev.next = nodeToInsert
        
            nodeToInsert.prev = node.prev
            nodeToInsert.next = node

            node.prev = nodeToInsert
            
            return

    


