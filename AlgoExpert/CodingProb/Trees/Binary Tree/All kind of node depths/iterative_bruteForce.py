def nodeDepth(root):
    stack = [(root, 0)]
    total_depth = 0

    while len(stack) > 0:
        node , depth = stack.pop()

        if node is None:
            continue

        total_depth += depth
        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))

    return total_depth
   

def allKindsOfNodeDepths(root):
    if not root:
        return

    all_node_depth = 0
    stack = [root]

    while len(stack) > 0:
        node = stack.pop()

        if node is None:
            continue

        all_node_depth += nodeDepth(node)

        stack.append(node.right)
        stack.append(node.left)

    return all_node_depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
