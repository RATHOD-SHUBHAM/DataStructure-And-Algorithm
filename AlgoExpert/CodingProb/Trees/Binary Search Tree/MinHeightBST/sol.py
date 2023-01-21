def minHeightBst(array):
    n = len(array)
    
    start = 0
    end = n - 1

    return constructBST(array, start, end)

def constructBST(array, start, end):
    if start > end:
        return

    mid = start + (end - start) // 2
    mid_node = array[mid]

    root = BST(mid_node)

    root.left = constructBST(array, start, mid - 1)
    root.right = constructBST(array, mid + 1, end)

    return root

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
