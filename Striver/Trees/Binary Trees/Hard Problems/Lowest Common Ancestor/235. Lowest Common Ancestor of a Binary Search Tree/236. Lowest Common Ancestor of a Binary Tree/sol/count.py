# Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.LCA = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.findAncestor(root, p, q)

        return self.LCA
    
    def findAncestor(self, node, p, q):
        # base case
        if not node:
            return 0
        
        left_val = self.findAncestor(node.left, p, q)
        right_val = self.findAncestor(node.right, p, q)

        cur_val = 0
        if node == p or node == q:
            cur_val = 1
        
        # if ancestor is found val will be 2
        if cur_val + left_val + right_val == 2:
            self.LCA = node
        
        return cur_val or left_val or right_val

        