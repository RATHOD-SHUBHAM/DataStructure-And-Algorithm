'''
Insertion 
A node can be added in four ways 
    1) Insert a node before a particular node .
    2) Insert a node after a particular node .
    3) At a particular position.

'''
class Node:
	def __init__(self,value):
		self.value = value
		self.next = None
		self.prev = None

class Dll:
	def __init__(self):
		self.head = None
		self.tail = None

	# set head
	def setHead(self,node):
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.insertBefore(self.head,node)

	# set tail
	def setTail(self,node):
		if self.tail == None:
			self.setHead(node)
		else:
			self.insertAfter(self.tail,node)


# 1.  Insert a node before a particular node

# here we will have to check are we trying to insert a already existing node -- 
	# if yes. then remove it from that place and add to a new place

	def insertBefore(self, beforethisNode, node):
		# if we are trying to insert a head or a tail node -- return because we cant set head and tail
		if node == self.head or node == self.tail:
			return

		# remove the node if it already exist
		self.removeNode(node)

		node.next = beforethisNode
		node.prev = beforethisNode.prev

		# if am trying to add before head node
		if beforethisNode.prev is None:
			self.head = node
		else:
			beforethisNode.prev.next = node

		beforethisNode.prev = node

# 2) Insert a node after a particular node .
def afterNode(self,afterThisNode,node):
	if node == self.head or node == self.tail:
		return

	self.remove(node)

	node.prev = afterThisNode
	node.next = afterThisNode.next

	if afterThisNode.next is None:
		self.tail = node
	else:
		afterThisNode.next.prev = node

	afterThisNode.next = node

# 3) At a particular position.
def insertAtPosition(self,node,K):
	if k == 1:
		self.setHead(node)
		return

	curNode = self.head
	pos = 1

	while curNode != None and pos != k:
		curNode = curNode.next
		pos += 1

	if curNode == None:
		self.setTail(node)
	elif pos == k:
		self.insertBefore(curNode,node)