# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = -math.inf
        high = math.inf

        if self.dfs(low, high, root) == True:
            return True
        else:
            return False
    
    def dfs(self, low, high, root):
        if not root:
            return
        
        if low < root.val and root.val < high:
            if self.dfs(low, root.val, root.left) == False:
                return False
            if self.dfs(root.val, high, root.right) == False:
                return False
        else:
            return False
        
        return True

