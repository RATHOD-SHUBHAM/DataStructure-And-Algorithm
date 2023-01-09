# Tc and Sc: O(n)
def iterativeInOrderTraversal(tree, callback):
    # op = []
    stack = []

    node = tree

    while node or len(stack) > 0:
        while node:
            stack.append(node)
            node = node.left
            
        curNode = stack.pop()
        # op.append(curNode)
        callback(curNode)
        node = curNode.right

    # return op
      