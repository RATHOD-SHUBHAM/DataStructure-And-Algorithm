# Tc ans Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both the nodes are not present
        if not p and not q:
            return True

        # only if one node is present
        if not p or not q:
            return False
        
        # If nodes doesnot have same values
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right , q.right)
