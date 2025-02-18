# Definition for a binary tree node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_height = -math.inf

        queue = [[root, 1]] # node, default node count

        while queue:
            node, height = queue.pop(0)

            max_height = max(max_height, height)

            if node.left:
                queue.append([node.left, height + 1])
            
            if node.right:
                queue.append([node.right, height + 1])
        
        return max_height
