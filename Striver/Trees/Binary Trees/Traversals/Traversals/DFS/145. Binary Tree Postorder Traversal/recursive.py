# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        op = []
        self.dfs(root, op)
        return op
    
    def dfs(self, root, op):
        # Left
        if root.left:
            self.dfs(root.left, op)
        
        # Right
        if root.right:
            self.dfs(root.right, op)
        
        # Root
        op.append(root.val)

        return