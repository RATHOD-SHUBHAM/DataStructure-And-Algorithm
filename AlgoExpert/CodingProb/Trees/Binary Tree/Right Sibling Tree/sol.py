# time = O(n) where n is the number of nodes in the tree
# space = O(d) where d is the depth of the tree

'''
2 pattern: first pattern for left child and 2nd for right child
1] left_child will point to parents right_child.
2] right_child will point to - parent's new right child's - left node
'''
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    parentNode = None # keep track of the parent Node
    isLeftChild = None # flag to indicate if the current node is the left child
    dfs(root, parentNode, isLeftChild)
    return root

def dfs(root, parentNode , isLeftChild):
    # base case
    if not root:
        return

    # keep a reference to move right as we will keep removing the right node
    rightChild = root.right

    # go left, all the way till leaf node
    dfs(root.left , root , True)

    if parentNode is None:
        root.right = None # remove the pointer to right node
    elif isLeftChild == True:
        # if the current node is the left child
        root.right = parentNode.right # pattern 1
    elif isLeftChild == False:
        if parentNode.right == None:
            root.right = None
        else:
            root.right = parentNode.right.left

    # traverse the right subtree
    dfs(rightChild , root , False)
