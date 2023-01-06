# Tc and Sc: O(h) and O(1)

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # if the node has a right node then successor will be
    # left most child of the right sub tree
    if node.right:
        return getLeftMostChild(node.right)

    return getAncestor(node)

def getLeftMostChild(node):
    while node.left:
        node = node.left

    return node

def getAncestor(node):
    # left child's right most element. so go on till we find the left ancestore
    while node.parent and node.parent.right == node:
        node = node.parent

    # this node will be the left child - return its parent
    return node.parent
