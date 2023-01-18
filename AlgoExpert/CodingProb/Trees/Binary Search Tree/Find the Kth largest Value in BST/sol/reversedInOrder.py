# time and space = O(n)

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# reverse Inorder traversal
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    reversedSortedArray = []
	reversedInorder(tree,k,reversedSortedArray)
	return reversedSortedArray[-1]

def reversedInorder(tree,k,reversedSortedArray):
	if not tree or len(reversedSortedArray) >= k:
		return
	reversedInorder(tree.right,k,reversedSortedArray)
	if len(reversedSortedArray) < k:
		reversedSortedArray.append(tree.value)
		reversedInorder(tree.left,k,reversedSortedArray)
	
