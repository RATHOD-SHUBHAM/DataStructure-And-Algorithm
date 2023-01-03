# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # max_path = 0 - passing a variable will not update the value
    max_path = [0]
    heightOfBT(tree, max_path)
    return max_path[0]

def heightOfBT(root, max_path):
    # base case
    if not root:
        return 0

    # get the left child height and right child height
    leftChild_height = heightOfBT(root.left, max_path)
    rightChild_height = heightOfBT(root.right, max_path)

    max_path[0] = max(max_path[0], leftChild_height + rightChild_height)

    # return height of the tree
    return 1 + max(leftChild_height , rightChild_height)

    
