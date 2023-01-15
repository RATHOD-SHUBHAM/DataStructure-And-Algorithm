# Time and Space = O(n)

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if not root:
        return
        
    curSum = 0
    branchSum = []
    traverseTree(root, curSum, branchSum)
    return branchSum

def traverseTree(root, curSum, branchSum):
    # get the sum including the current node
    newSum = curSum + root.value

    # check if this is the leaf node
    if not root.left and not root.right:
        branchSum.append(newSum)
        return 

    if root.left:
        traverseTree(root.left, newSum, branchSum)

    if root.right:
        traverseTree(root.right, newSum, branchSum)

    return
