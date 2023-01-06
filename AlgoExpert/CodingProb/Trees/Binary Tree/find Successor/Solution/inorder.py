# Tc and Sc: O(n)

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    inorder_array = inorderTraversal(tree)
    # print("inorder_array : ", inorder_array)

    n = len(inorder_array)

    for i in range(n):
        curNode = inorder_array[i]

        if curNode == node:
            return inorder_array[i + 1] if (i + 1) < n else None



def inorderTraversal(root):
    op = []
    stack = []

    node = root

    while node or len(stack) > 0:
        # go to the left left node
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        op.append(node)
        node = node.right

    return op
