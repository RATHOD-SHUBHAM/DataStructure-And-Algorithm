# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    root = BST(preOrderTraversalValues[0])
    constructBST(preOrderTraversalValues, root)

    return root

def constructBST(array, root):
    n = len(array)
    stack = [root]

    for i in range(1, n):
        child = array[i]
        childNode = BST(child)

        parentNode = stack[-1]

        while stack and stack[-1].value <= childNode.value:
            parentNode = stack.pop()

        if parentNode.value <= childNode.value:
            parentNode.right = childNode
        else:
            parentNode.left = childNode

        stack.append(childNode)

    return