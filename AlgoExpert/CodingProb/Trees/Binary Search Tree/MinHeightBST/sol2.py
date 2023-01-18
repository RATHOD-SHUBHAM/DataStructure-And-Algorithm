# Time and Space = O(n)

def minHeightBst(array):
    return constructBST(array,0,len(array)-1)

def constructBST(array,left,right):
	if left > right:
		return
	
	mid = left + (right - left)//2
	
	tree = BST(array[mid]) # create a node
	
	tree.left = constructBST(array,left,mid - 1)
	tree.right = constructBST(array,mid + 1,right)
	
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
