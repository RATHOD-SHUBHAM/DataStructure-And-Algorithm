'''

572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if t is None: return True
        if s is None and t is not None: return False

        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s, t) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)