# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and not q:
            return False
        
        if q and not p:
            return False
        
        if p.val != q.val:
            return False
        
        same_left = self.isSameTree(p.left, q.left)
        same_right = self.isSameTree(p.right, q.right)

        if same_left == False or same_right == False:
            return False
        else:
            return True