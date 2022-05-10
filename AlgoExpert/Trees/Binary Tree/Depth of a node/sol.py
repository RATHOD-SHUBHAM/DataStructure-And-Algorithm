# depth of node x in tree.

# Python3 program to find distance of
# a given node from root.

# A class to create a new Binary
# Tree Node
class newNode:
	def __init__(self, item):
		self.data = item
		self.left = self.right = None

# Returns -1 if x doesn't exist in tree.
# Else returns distance of x from root
def findDistance(root, x):
	
	# Base case
	if (root == None):
		return -1

	# Initialize distance
	dist = -1

	# Check if x is present at root or
	# in left subtree or right subtree.
	if (root.data == x):
		return dist + 1
	else:
		dist = findDistance(root.left, x)
		if dist >= 0:
			return dist + 1
		else:
			dist = findDistance(root.right, x)
			if dist >= 0:
				return dist + 1

	return dist

# Driver Code
if __name__ == '__main__':

	root = newNode(5)
	root.left = newNode(10)
	root.right = newNode(15)
	root.left.left = newNode(20)
	root.left.right = newNode(25)
	root.left.right.right = newNode(45)
	root.right.left = newNode(30)
	root.right.right = newNode(35)

	print(findDistance(root, 45))

# This code is contributed by PranchalK
