# time = O(nlogn) 
# space = O(n)


# brute force approach
from collections import deque
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# calculate depth
def sumOfDepth(node,depth = 0):
	if not node:
		return 0
	leftNode = sumOfDepth(node.left , depth + 1)
	rightNode = sumOfDepth(node.right,depth + 1)
	
	return depth + leftNode + rightNode

# calculate depth of each node and add those depth
def allKindsOfNodeDepths(root):
    # Write your code here.
	if not root:
		return 

	sum_of_all_depth = 0

	stack = deque([root])

	while stack:
		node = stack.popleft()

		if not node:
			continue

		sum_of_all_depth += sumOfDepth(node)

		stack.append(node.left)
		stack.append(node.right)

	return sum_of_all_depth





