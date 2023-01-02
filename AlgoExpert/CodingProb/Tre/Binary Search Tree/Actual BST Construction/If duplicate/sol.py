# O(n)
# learnt it from leetcode

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
		return None
        
	root = BST(preOrderTraversalValues[0])
	stack = [root]

	for i in range(1, len(preOrderTraversalValues)):
		parentNode = stack[-1]
		nodeToadd = BST(preOrderTraversalValues[i])

		while stack and stack[-1].value <= nodeToadd.value:
			parentNode = stack.pop()

		if nodeToadd.value < parentNode.value:
			parentNode.left = nodeToadd
		else:
			parentNode.right = nodeToadd

		stack.append(nodeToadd)

	return root
