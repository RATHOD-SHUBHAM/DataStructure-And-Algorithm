# Time = O(n) n = number of nodes in tree
# Space = O(d)  d is the depth of the tree

# This is an input class. Do not edit.
import math
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    minNode = -math.inf
	maxNode = math.inf
	return helper(tree,minNode,maxNode)

def helper(tree,min_node,max_node):
	if not tree:
		return True
	
	if tree.value >= max_node or tree.value < min_node:
		return False
	
	left = helper(tree.left,min_node,tree.value)
	right = helper(tree.right,tree.value,max_node)
	
	return left and right