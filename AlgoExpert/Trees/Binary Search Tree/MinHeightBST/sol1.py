# Time and space = O(nlogn) || O(n)
# array should be sorted and should be unique
def minHeightBst(array):
	left = 0
	right = len(array) - 1
    return constructBST(array,None,left,right)

def constructBST(array,tree,left,right):
	if left > right:
		return
	
	mid = left + (right - left)//2
	
	value = array[mid]
	
	if not tree:
		tree = BST(value)
	else:
		tree.insert(value)
		
	constructBST(array,tree,left,mid - 1)
	constructBST(array,tree,mid + 1,right)
	
	return tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
