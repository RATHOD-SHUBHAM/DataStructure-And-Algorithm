
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    # Code here -> p = zero based -> Insert after P
    
    new_node = Node(data)
    
    if p == 0:
        new_node.next = head.next
        
        if head.next is not None:
            head.next.prev = new_node
            
        head.next = new_node
        new_node.prev = head
        
        return head
        
    curNode = head
    prevNode = None
    curPos = 0
    
    while curNode and curPos < p:
        prevNode = curNode
        curNode = curNode.next
        curPos += 1
    
    if curNode == None:
        prevNode.next = new_node
        new_node.prev = prevNode
        return head
    else:
        # Add new Node
        new_node.prev = curNode
        new_node.next = curNode.next
        
        if curNode.next:
            curNode.next.prev = new_node
            
        curNode.next = new_node
        return head