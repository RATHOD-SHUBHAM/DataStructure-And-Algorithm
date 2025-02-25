# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False
        
        return self.dfs(root.left, root.right)
    
    def dfs(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        
        if not root_1 or not root_2:
            return False
        
        return root_1.val == root_2.val and self.dfs(root_1.left, root_2.right) and self.dfs(root_2.left, root_1.right)
    

    # -------------- Same solution different way to write ----------------
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)
    
    def check(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False
        
        return self.check(p.left, q.right) and self.check(p.right, q.left)