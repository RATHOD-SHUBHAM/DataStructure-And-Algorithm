# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        op = []
        level = 0
        self.bfs(root, level, op)
        return op
    
    
    def bfs(self, root, level, op):
        if not root:
            return op
        
        # adding a new level
        if len(op) == level:
            op.append([])
            
        # append the node to the op based on its level
        op[level].append(root.val)
        
        if root.left:
            self.bfs(root.left , level + 1 , op)
            
        if root.right:
            self.bfs(root.right , level + 1 , op)
            
        return op
            