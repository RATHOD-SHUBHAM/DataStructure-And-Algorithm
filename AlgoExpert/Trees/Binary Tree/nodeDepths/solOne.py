
# O(n) || O(h)
def nodeDepths(root):
    # Write your code here.
    if not root:
		return 0
	
	depth = 0
	return helper(root, depth)

def helper(root,depth):
	if not root:
		return 0
	
	leftNode = helper(root.left, depth+1)
	rightNode = helper(root.right, depth + 1)
	
	return depth + leftNode + rightNode


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
