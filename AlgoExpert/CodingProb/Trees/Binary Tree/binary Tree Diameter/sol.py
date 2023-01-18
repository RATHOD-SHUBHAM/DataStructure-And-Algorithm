# same solution on leetcode
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    diameter = [0]
	helper(tree,diameter)
	return diameter[0]

def helper(root, diameter):
	if not root:
		return -1
	
	leftTree_height = helper(root.left, diameter)
	rightTree_height = helper(root.right, diameter)
	
	curDiameter = 2 + leftTree_height + rightTree_height
	
	diameter[0] = max(diameter[0], curDiameter)
	
	return 1 + max(leftTree_height, rightTree_height)
