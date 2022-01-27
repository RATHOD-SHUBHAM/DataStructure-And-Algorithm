# Time = average - O(log n) | worst - O(n)
# space = O(1)

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		curNode = self
		
		while True:
			if value < curNode.value:
				if not curNode.left:
					# if there is no element on left -- add the element to left
					curNode.left = BST(value) 
					break
				else:
					curNode = curNode.left
			else:
				if not curNode.right:
					curNode.right = BST(value)
					break
				else:
					curNode = curNode.right
					
        return self

    def contains(self, value):
        # Write your code here.
        curNode = self
		
		while curNode:
			if value < curNode.value:
				curNode = curNode.left
			elif value > curNode.value:
				curNode = curNode.right
			else:
				return True
		return False

    def remove(self, value, parentNode = None):
        # Write your code here.
        # Do not edit the return statement of this method.
		curNode = self
		
		while curNode:
			# step 1 = search
			if value < curNode.value:
				parentNode = curNode
				curNode = curNode.left
			elif value > curNode.value:
				parentNode = curNode
				curNode = curNode.right

			else: # value found to be deleted
				# case1 : when node has 2 child
				if curNode.left and curNode.right:
					# get the smallest value from right tree
					curNode.value = curNode.right.getMin()
					# delete the smallest node
					curNode.right.remove(curNode.value,curNode) # if there are only 2 node and i want to delete parent,
					# then there should be a way for me the replace the parent with child node and delete child.
					# tracking can be done using parent node as reference
					
				# case 2: when there is only one child
				# case a: when it has no parent
				elif parentNode is None:
					# order is important
					if curNode.left:
						curNode.value = curNode.left.value
						curNode.right = curNode.left.right
						curNode.left = curNode.left.left
						
					elif curNode.right:
						curNode.value = curNode.right.value
						curNode.left = curNode.right.left
						curNode.right = curNode.right.right
					else: #if this is a single node
						pass
				# case 2: when there is only one child
				# case b: when it a node in between
				elif parentNode.left == curNode:
					parentNode.left = curNode.left if curNode.left else curNode.right
				elif parentNode.right == curNode:
					parentNode.right = curNode.left if curNode.left else curNode.right
				break
	
        return self
	
	def getMin(self):
		curNode = self
		
		while curNode.left:
			if curNode.left:
				curNode = curNode.left
		return curNode.value
