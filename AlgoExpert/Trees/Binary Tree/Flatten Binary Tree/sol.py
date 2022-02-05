'''
rightmost child		 				Leftmost child
of				---> root Node ---> of
leftsubtree							rightsubtree

'''

# Time and Space Complexity: O(n) || O(d) where n is the number of nodes in the tree and d is the depth of the tree

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
	leftmost, rightmost = helper(root)
	return leftmost

def helper(root):
    # left child
	if not root.left:
		leftmost = root
	else:
		leftmostchild, rightmostchild = helper(root.left)
		# connect rightmost child of left subtree to root
		connect(rightmostchild, root)
		# send left most child to parent
		leftmost = leftmostchild
		
	# right child
	if not root.right:
		rightmost = root
	else:
		leftmostchild, rightmostchild = helper(root.right)
		# connect leftmost child of right subtree to root
		connect(root, leftmostchild)
		# send the rightmost child to parent
		rightmost = rightmostchild
	
	return [leftmost, rightmost]

def connect(nodeOne, nodeTwo):
	nodeOne.right = nodeTwo
	nodeTwo.left = nodeOne
