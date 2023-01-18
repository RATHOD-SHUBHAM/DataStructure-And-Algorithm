# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    # Write your code here.
    return checkSymmetry(tree.left, tree.right)

def checkSymmetry(leftNode, rightNode):
    # base case
    if not leftNode and not rightNode:
        return True
        
    if not leftNode or not rightNode:
        return False

    if leftNode.value != rightNode.value:
        return False

    # check the border and inner nodes
    if checkSymmetry(leftNode.left, rightNode.right) and checkSymmetry(leftNode.right, rightNode.left):
        return True
    else:
        return False