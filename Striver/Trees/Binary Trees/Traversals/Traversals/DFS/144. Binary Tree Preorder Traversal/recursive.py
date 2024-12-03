# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        op = []
        self.dfs(root, op)
        return op
    
    def dfs(self, root, op):
        op.append(root.val)

        if root.left:
            self.dfs(root.left, op)
        if root.right:
            self.dfs(root.right, op)
        
        return