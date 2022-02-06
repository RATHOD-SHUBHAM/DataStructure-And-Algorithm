'''
						 node depth of left subtree + no of node on left subtree 
sum of all nodes depth =								+
						 node depth of right subtree + no of nodes on right subtree
'''	

# time and space = O(n)

def allKindsOfNodeDepths(root):
	# this will give count of all node from particular node
    nodeCount = {}
	no_of_nodes(root, nodeCount)
	
	# count the depth of all node from particular node
	nodeDepth = {}
	depth_of_all_nodes(root,nodeDepth,nodeCount)
	
	# sum depth of all node
	return sumOfAllNodesDepth(root, nodeDepth)
	
		
	
def no_of_nodes(root, nodeCount):
	# for curNode count is 1
	nodeCount[root] = 1 # initialize the root node
	
	if root.left:
		no_of_nodes(root.left,nodeCount)
		# update the root node with no of nodes on left subtree
		nodeCount[root] += nodeCount[root.left]
		
	if root.right:
		no_of_nodes(root.right,nodeCount)
		# update the root node with no of nodes on right subtree
		nodeCount[root] += nodeCount[root.right]
		
		
def depth_of_all_nodes(root,nodeDepth,nodeCount):
	# for curNode depth is 0
	nodeDepth[root] = 0
	
	if root.left:
		depth_of_all_nodes(root.left,nodeDepth,nodeCount)
		# nodes depth = depth of left subtree + no of nodes on left subtree
		nodeDepth[root] += nodeDepth[root.left] + nodeCount[root.left]
		
	if root.right:
		depth_of_all_nodes(root.right,nodeDepth,nodeCount)
		# nodes depth = depth of right subtree + no of right on left subtree
		nodeDepth[root] += nodeDepth[root.right] + nodeCount[root.right]
		

def sumOfAllNodesDepth(root, nodeDepth):
	if not root:
		return 0
	
	curNodeDepth = nodeDepth[root]
	depthOfLeftChild = sumOfAllNodesDepth(root.left, nodeDepth)
	depthOfRightChild = sumOfAllNodesDepth(root.right, nodeDepth)
	
	return curNodeDepth + depthOfLeftChild + depthOfRightChild
	
	
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
