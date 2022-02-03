# This is an input class. Do not edit.
# time and space = O(n) || O(n)
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right


def findSuccessor(tree, node):
    # Write your code here.
    inorder = inorderTraversal(tree)
	
	for i in range(len(inorder)):
		if i == len(inorder) - 1:
			return None
		elif inorder[i] == node:
			return inorder[i+1]
		
def inorderTraversal(tree, order = []):
	if not tree:
		return
	
	inorderTraversal(tree.left,order)
	order.append(tree)
	inorderTraversal(tree.right,order)
	
	return order
	
