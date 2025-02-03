# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ancestor = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ancestor
    
    def dfs(self, root, p , q):
        if not root:
            return False
        
        # If the current node is one of p or q node.
        root_val = False # this is just initialization
        if root == p or root == q:
            root_val = True
        
        left_val = self.dfs(root.left, p, q)
        right_val = self.dfs(root.right, p, q)

        # If at any point any of two of the three flags left_val, right_val or root_val become True. 
        # Then we have found the ancestor
        if root_val + left_val + right_val >= 2:
            self.ancestor =  root
        
        # return the true value, if any of them are p or q
        return root_val or left_val or right_val
