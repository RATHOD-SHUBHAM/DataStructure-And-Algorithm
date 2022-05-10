"""
	set head has 4 scenario:
		1. If the node is already present as head node -> dont do anything just return.
		2. If this node is the first ele of DLL => then the node will be both head and tail.
		3. If there is head node already present(and this is the only node that is present) -> add node in front of head.
		4. Node can be already present -> there can be 2 cases:
			a. It will be present as tail
			b. somewhere in btn  /or/  adding new node as head



	Remove tail:
		1. If there is no node -- return
		2. If there is only one node present -- make it None
		3. if there are more than one node.

"""


class DoubleLinkListNode:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None

class DoubleLinkList:
	def __init__(self):
		self.head = None
		self.tail = None
		
	def setHead(self,node):
		"""
			set head has 4 scenario:
				1. If the node is already present as head node -> dont do anything just return.
				2. If this node is the first ele of DLL => then the node will be both head and tail.
				3. If there is head node already present(and this is the only node that is present) -> add node in front of head.
				4. Node can be already present -> there can be 2 cases:
					a. It will be present as tail
					b. somewhere in btn  /or/  adding new node as head
		"""
		# scenario 1:
		if self.head == node:
			return
		
		# scenario 2:
		elif self.head is None:
			self.head = node
			self.tail = node
			
		# scenario 3:
		elif self.head == self.tail:
			self.tail.prev = node
			self.head = node
			self.head.next = self.tail
		
		#scenario 4:
		else:
			if self.tail == node:
				self.removeTail()
			self.removeConnection(node)
			self.head.prev = node
			node.next = self.head
			self.head = node
	
	def removeTail(self):
		'''
		Remove tail:
			1. If there is no node -- return
			2. If there is only one node present -- make it None
			3. if there are more than one node.
		'''
		if self.tail is None:
			return
		if self.tail == self.head:
			self.head = None
			self.tail = None
			return
		self.tail = self.tail.prev
		self.tail.next = None
		
	def removeConnection(self,node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None