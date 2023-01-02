# Brute force 
# time and space = O(n)
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    inorder = inorderTraversal(root,[])
	
	for i in range(len(inorder) - 1):
		leftNode = inorder[i]
		rightNode = inorder[i+1]
		connect(leftNode,rightNode)
		
	return inorder[0]


def connect(leftnode, rightnode):
	leftnode.right = rightnode
	rightnode.left = leftnode
	
	
def inorderTraversal(root,op):
	if not root:
		return
	inorderTraversal(root.left,op)
	op.append(root)
	inorderTraversal(root.right,op)
	
	return op
		
