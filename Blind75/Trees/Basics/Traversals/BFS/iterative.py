# BFS is always associated with a Queue.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        op = []
        level = 0
        queue = [[root , level]]
        
        while queue:
            node, level = queue.pop(0)
            
            # add a new level
            if level == len(op):
                op.append([])
                
            # append the current node to that level
            op[level].append(node.val)
            
            if node.left:
                queue.append([node.left, level + 1])
            
            if node.right:
                queue.append([node.right, level + 1])
        
        return op