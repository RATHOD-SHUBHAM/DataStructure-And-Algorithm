# time = O(n) where n is the number of nodes in the tree
# space = O(d) where d is the depth of the tree

'''
left child -- points to right child of parent
right child -- points to left child of parents sibling

First update the left child
then the parent child 
then the right child

If a node does not have any parent.
then its right child will point to none

'''
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    helper(root,None,None)
	return root

def helper(root,parent,isLeftChild):
	if not root:
		return
	
	# keep reference -- becasue we will change the pointers
	leftChild = root.left
	rightChild = root.right
	
	# first change the pointer of leftchild
	helper(leftChild, root, True)
	
	# change the pointers of root node
	if parent is None:
		root.right = None
	# if the node is a left child
	elif isLeftChild:
		root.right = parent.right
	# if right child
	elif not isLeftChild:
		# if parent doesnot have a right sibling
		if parent.right is None:
			root.right = None
		else:
			root.right = parent.right.left
			
	# change the pointer for right node
	helper(rightChild, root, False)
	
