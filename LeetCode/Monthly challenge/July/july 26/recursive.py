# Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ref = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recurse(node):
            if not node:
                return False
            
            
            left = recurse(node.left) 
            
            
            right = recurse(node.right)
            
            
            
            mid = node == p or node == q
            
            
            if mid + left + right >= 2:
                self.ref = node # I am saving this because when I return I might end up one of the left portion and continue with the right node
            
            return mid or left or right
        
        recurse(root)
        return self.ref