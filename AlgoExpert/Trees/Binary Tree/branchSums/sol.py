# Time and Space = O(n)

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	result = [] # create a list to store sum
    calculateSum(root,0,result) # recursively call the element from each node
	
	return result

def calculateSum(node,currentSum,result):
	if node is None: # if it is a unbalanced binary tree
		return
	
	
	currentSum += node.value
	
	if node.left is None and node.right is None:
		result.append(currentSum)
		return
	
	calculateSum(node.left,currentSum,result)
	calculateSum(node.right,currentSum,result)
