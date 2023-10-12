# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        op= []
        level = 0

        self.bfs(root, op, level)

        return op

    def bfs(self, node, op, level):
        if not node:
            return
        
        if len(op) == level:
            op.append([])
        
        op[level].append(node.val)


        self.bfs(node.left, op, level + 1)
        self.bfs(node.right, op, level + 1)

        return op