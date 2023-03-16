# Time and space = O(h + k) and O(h)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

		
class TreeInfo:
	def __init__(self,no_of_nodes_visited,last_visited_node):
		self.no_of_nodes_visited = no_of_nodes_visited
		self.last_visited_node = last_visited_node

def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0,0)
	reversedInorder(tree,k,treeInfo)
	return treeInfo.last_visited_node

def reversedInorder(tree, k ,treeInfo):
	if not tree or treeInfo.no_of_nodes_visited >= k:
		return
	reversedInorder(tree.right, k ,treeInfo)
	
	if treeInfo.no_of_nodes_visited < k:
		treeInfo.no_of_nodes_visited += 1
		treeInfo.last_visited_node = tree.value
		reversedInorder(tree.left, k ,treeInfo)
	
