# Tc and Sc: O(n)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    n = len(preOrderTraversalValues)

    # Make the first value as root node
    root_node = preOrderTraversalValues[0]
    root = BST(root_node)

    # add the node to stack
    stack = [root]

    # traverse for child node
    for i in range(1, n):
        child = preOrderTraversalValues[i]
        child_node = BST(child)
        parent_node = stack[-1]

        # if my current node is lesser than stacks top element - then we have found the parent
        # keep clearing stack as long as we find the parent node
        while stack and child_node.value >= stack[-1].value:
            parent_node = stack.pop()

        if child_node.value < parent_node.value:
            parent_node.left = child_node
        else:
            parent_node.right = child_node

        # append the child to stack
        stack.append(child_node)

    return root
