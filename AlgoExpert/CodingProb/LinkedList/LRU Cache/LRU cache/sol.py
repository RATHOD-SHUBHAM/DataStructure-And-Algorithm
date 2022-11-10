# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
		# hash to access the node in o(1)
		self.hashmap = {}
		# len to check we didnt max out the length if LL
		self.len = 0
		# double LL to keep track of most recent and least recently visited
		self.dll = DoubleLinkedList()

    def insertKeyValuePair(self, key, value):
        # Write your code here.
		if key not in self.hashmap:
			if self.maxSize == self.len:    # when my linkedlist is full
				self.removeLeastVisited()
			else:
				self.len += 1
			
            self.hashmap[key] = DoubleLinkedListNode(key,value)
			
		else:
			self.replaceKey(key,value)
		
        self.updateRecentlyVisited(self.hashmap[key])
		
		
	def removeLeastVisited(self):
		# remove the tail
		nodetoremove = self.dll.tail.key # make a copy of the key value, so that it will be useful in removing it from hashmap
		self.dll.removeTail()
		# delete the key value pair from hash
		del self.hashmap[nodetoremove]
		
		
	def replaceKey(self,key,value):
		if key not in self.hashmap:
			raise Exception(" Key not present in hash map")
		# just update the value for that key
		self.hashmap[key].value = value
		
	def updateRecentlyVisited(self, node):
		self.dll.sethead(node)

    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.hashmap:
			return None
		self.updateRecentlyVisited(self.hashmap[key])
		return self.hashmap[key].value

    def getMostRecentKey(self):
        # Write your code here.
        if self.dll.head is None:
			return None
		return self.dll.head.key
	
	
class DoubleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		
		
	def sethead(self,node):
		# if the node is the first element and head
		if self.head == node:
			return
		# if it is the first element to be inserted
		elif self.head is None:
			self.head = node
			self.tail = node
		# inserting new element and making it as a head
		elif self.head == self.tail:
			self.tail.prev = node
			self.head = node
			self.head.next = self.tail
		# once visited if my node is at tail. ill have to remove it from there and make it head
		else:
			if self.tail == node:
				self.removeTail()
			node.removeBinding()
			self.head.prev = node
			node.next = self.head
			self.head = node
			
	def removeTail(self):
		if self.tail is None:
			return
		if self.tail == self.head:
			self.head = None
			self.tail = None
			return
		self.tail = self.tail.prev
		self.tail.next = None
		
		
class DoubleLinkedListNode:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None
	
	def removeBinding(self):
		# remove the node
		if self.prev is not None:
			self.prev.next = self.next
		if self.next is not None:
			self.next.prev = self.prev
		self.prev = None
		self.next = None
		