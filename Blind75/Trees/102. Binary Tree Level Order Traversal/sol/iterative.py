# BFS is always associated with a queue data structure.

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

        stack = [[root, level]]

        while stack:
            node, level = stack.pop(0)

            if level == len(op):
                op.append([])
            
            op[level].append(node.val)

            if node.left:
                stack.append([node.left , level + 1])
            
            if node.right:
                stack.append([node.right , level + 1])
        
        return op