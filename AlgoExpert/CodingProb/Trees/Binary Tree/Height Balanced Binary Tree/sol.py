# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    treeHeight, isBalanced = heightBalanced(tree)
    return isBalanced

def heightBalanced(root):
    if not root:
        return (0, True)

    leftChild_height, leftChild_isBalanced = heightBalanced(root.left)
    rightChild_height , rightChild_isBalanced = heightBalanced(root.right)

    curtree_height = 1 + max(leftChild_height, rightChild_height)
    
    if abs(rightChild_height - leftChild_height) > 1:
        return (curtree_height, False)

    if not leftChild_isBalanced or not rightChild_isBalanced:
        return (curtree_height , False)

    return (curtree_height, True)
    
