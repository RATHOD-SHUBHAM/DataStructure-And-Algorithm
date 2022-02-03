'''
Inorder traversal = left --> root --> right

1] so if we are at root. Then our successor will be the right element
		Case 1] if right node has a child then
		root --> (left root right)
		right nodes left most element wil be successor of root.
2] since left child cant be a successor. Some time ancestor will be a successo

	root1 --> (left root2 right)
	so if we are at right we have to go all the way up to root1

'''
# time = O(n)
# sapce = O(1)
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # if the node has right child. The right childs left most child is successor
	if node.right:
		return getLeftmostChild(node.right)
	# else return ancestor
	return ancestor(node)

def getLeftmostChild(node):
	while node.left:
		node = node.left
	return node

def ancestor(node):
	while node.parent and node.parent.right == node:
		node = node.parent
		
	return node.parent
	
