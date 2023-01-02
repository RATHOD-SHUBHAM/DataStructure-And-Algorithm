'''
if right insertion
no of smaller nodes = no of left subtree + curNode

if left :
no of subtree + 1

'''
# Timne = O(nlog(n))
# space =O(n)


def rightSmallerThan(array):
    if len(array) == 0:
		return []
	
	smaller = array[:]
	
	lastIdx = len(array) - 1
	
	# creating tree - adding root node
	bst = BST(array[lastIdx],lastIdx,0)
	
	for i in reversed(range(lastIdx)):
		bst.insert(array[i],i)
		
	getSmaller(bst,smaller)
	
	return smaller

def getSmaller(bst,smaller):
	if not bst:
		return
	smaller[bst.idx] = bst.smallerNodeCount
	getSmaller(bst.left,smaller)
	getSmaller(bst.right,smaller)

class BST:
	def __init__(self,value,idx,smallerNodeCount):
		self.value = value
		self.left = None
		self.right = None
		self.idx = idx
		self.left_subtree_count = 0
		self.smallerNodeCount = smallerNodeCount
		
	def insert(self,value,idx,smallerNodeCount = 0):
		if value < self.value:
			self.left_subtree_count += 1
			if not self.left:
				self.left = BST(value,idx,smallerNodeCount)
			else:
				self.left.insert(value,idx,smallerNodeCount)
		else: # am going right
			# if value is equal to current node
			smallerNodeCount += self.left_subtree_count
			# if value is greater than current node
			if value > self.value:
				smallerNodeCount += 1
			if not self.right:
				self.right = BST(value,idx,smallerNodeCount)
			else:
				self.right.insert(value,idx,smallerNodeCount)