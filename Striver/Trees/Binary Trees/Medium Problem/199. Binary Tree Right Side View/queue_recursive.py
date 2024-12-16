# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
If level == len(op):
    Then this node is being encounterd for the first time
'''
class Solution:
    def __init__(self):
        self.op = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        level = 0
        self.dfs(root, level)

        return self.op
        
    def dfs(self, root, level):
        """Root >> Right >> Left"""
        if not root:
            return
        
        # Root
        if level == len(self.op):
            self.op.append(root.val)
            
        # Right
        self.dfs(root.right, level + 1)

        # Left
        self.dfs(root.left, level + 1)
        
        return