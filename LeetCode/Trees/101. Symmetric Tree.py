'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:



'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.helper(root.left, root.right)

    def helper(self, leftChild, rightChild):
        if leftChild and rightChild:  # is not None
            return leftChild.val == rightChild.val and self.helper(leftChild.left, rightChild.right) and self.helper(
                leftChild.right, rightChild.left)

        return leftChild == rightChild
