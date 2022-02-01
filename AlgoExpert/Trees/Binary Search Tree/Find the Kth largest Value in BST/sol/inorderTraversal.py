# Time and Space = O(n)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# inorder traversal will give sorted array
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    sortedArray = []
	inOrder(tree,sortedArray)
	return sortedArray[len(sortedArray) - k]

def inOrder(tree,sortedArray):
	if not tree:
		return
	
	inOrder(tree.left,sortedArray)
	sortedArray.append(tree.value)
	inOrder(tree.right,sortedArray)
	
	
