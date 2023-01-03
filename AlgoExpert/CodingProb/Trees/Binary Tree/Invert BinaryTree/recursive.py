def invertBinaryTree(tree):
    if not tree:
        return

    if not tree.left and not tree.right:
        return

    # swap the child of the tree
    swapTree(tree)

    # Move to the children and swap their child
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

    return

def swapTree(root):
    root.left , root.right = root.right, root.left
    return

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
