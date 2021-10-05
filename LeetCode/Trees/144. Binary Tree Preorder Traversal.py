'''
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return

        stac_k = [root]
        result = []

        while stac_k != []:
            root = stac_k.pop()
            result.append(root.val)

            if root.right:
                stac_k.append(root.right)

            if root.left:
                stac_k.append(root.left)

        return result