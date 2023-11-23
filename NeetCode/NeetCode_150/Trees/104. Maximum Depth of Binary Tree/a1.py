# Recursive Method --------------------------------------------------------

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

        left_subTree_depth = self.maxDepth(root.left)
        right_subTree_depth = self.maxDepth(root.right)

        return 1 + max(left_subTree_depth , right_subTree_depth)
        

# Iterative Method --------------------------------------------------------------

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

        # node, depth
        queue = [(root, 1)]

        max_depth = 1

        while queue:
            node, depth = queue.pop(0)

            max_depth = max(max_depth, depth)

            if node.left:
                queue.append((node.left , depth + 1))
            
            if node.right:
                queue.append((node.right , depth + 1))
        
        return max_depth