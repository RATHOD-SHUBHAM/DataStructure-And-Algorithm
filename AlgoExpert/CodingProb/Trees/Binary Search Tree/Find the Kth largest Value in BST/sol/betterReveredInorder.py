# Tc : O(h + k) | Sc: O(h)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# REVERSED INORDER
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    reversed_inorder = reversedInOrder(tree, k)
    print("reversed_inorder : ",reversed_inorder)
    return reversed_inorder[- 1]

def reversedInOrder(root , k):
    op = []
    stack = []

    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.right

        curNode = stack.pop()

        # just check for K value
        if len(op) < k:
            op.append(curNode.value)
            node = curNode.left
        else:
            break

    return op