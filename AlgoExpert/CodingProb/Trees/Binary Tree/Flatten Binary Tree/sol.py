# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    op = []
    inorder_array = inorderTraversal(root, op)
    n = len(inorder_array)

    for i in range(1, n):
        leftNode = inorder_array[i - 1]
        rightNode = inorder_array[i]
        connect(leftNode , rightNode)

    return inorder_array[0]


# Inorder using recursion
def inorderTraversal(root, op):
    if not root:
        return

    inorderTraversal(root.left, op)
    op.append(root)
    inorderTraversal(root.right, op)

    return op

# connecting left and right node
def connect(leftNode , rightNode):
    leftNode.right = rightNode
    rightNode.left = leftNode
