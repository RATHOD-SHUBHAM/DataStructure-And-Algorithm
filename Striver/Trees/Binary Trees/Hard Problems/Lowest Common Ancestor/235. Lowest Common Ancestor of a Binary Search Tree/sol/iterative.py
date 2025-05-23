'''
    We can solve this using the approaches to find LCA in a binary tree.

    But, binary search tree's property could be utilized, to come up with a better algorithm.


    When the nodes (p and q) split, Then root will always be their ancestor.

'''

# Tc Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return []

        while root:

            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        