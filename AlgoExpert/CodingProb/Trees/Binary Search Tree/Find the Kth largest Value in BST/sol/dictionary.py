# Time and space = O(h + k) and O(h)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    dic = {
			'no_of_nodes_visited' : 0,
			'last_visited' : None
		  }
	
	reversedInorder(tree,k,dic)
	return dic['last_visited']

def reversedInorder(tree,k,dic):
	if not tree or dic["no_of_nodes_visited"] >= k:
		return
	
	reversedInorder(tree.right, k ,dic)
	
	if dic["no_of_nodes_visited"] < k:
		dic["no_of_nodes_visited"] = dic["no_of_nodes_visited"]+1
		dic["last_visited"] = tree.value
		reversedInorder(tree.left, k ,dic)