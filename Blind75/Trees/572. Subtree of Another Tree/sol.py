# Tc: O(mn) | Sc: O(m + n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # When both are None - they are the same
        if not root and not subRoot:
            return True
        
        # When subroot is present but root is empty
        if not root and subRoot:
            return False
        
        # Compare subroot to leaf node of root
        if root and not subRoot:
            return True
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def sameTree(self, p, q):
        # When both are None - they are the same
        if not p and not q:
            return True
        
        # When subroot is present but root is empty
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)