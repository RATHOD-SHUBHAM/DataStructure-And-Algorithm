# Tc and Sc: O(n)

def invertBinaryTree(tree):
    stack = [tree]

    while len(stack) > 0:
        root = stack.pop()

        if root is None:
            continue

        root.left , root.right = root.right, root.left

        stack.append(root.left)
        stack.append(root.right)

    return
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
