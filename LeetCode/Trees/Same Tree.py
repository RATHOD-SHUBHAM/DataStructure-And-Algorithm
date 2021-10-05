"""
100. Same Tree
Easy

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if both tree has nothing in them then it is the same
        # if not p means. if p is null or None
        if not p and not q:
            return True

        # if p has value and q is none then both tree are not same and vice versa
        if not p or not q:
            return False

        # if p has value and it is same as that of q values then check for it children else return  false
        if p.val != q.val:
            return False

        # if parents values are same check its children value
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
