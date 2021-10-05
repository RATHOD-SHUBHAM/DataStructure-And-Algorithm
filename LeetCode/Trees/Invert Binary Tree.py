"""

226. Invert Binary Tree
Easy

Invert a binary tree.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if there is nothing at node return None
        if not root:
            return None
        # move to its child
        self.invertTree(root.right)
        self.invertTree(root.left)
        # swap children
        root.left, root.right = root.right, root.left

        return root
