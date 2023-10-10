# Same as Height of tree.

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


        left_tree_height = self.maxDepth(root.left)
        right_tree_height = self.maxDepth(root.right)

        return 1 + max(left_tree_height , right_tree_height)
    
# ------------------------------------------------------------------------------

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

        max_depth = 0     
        cur_depth = 1

        stack = []
        stack.append([cur_depth, root])

        while stack:
            cur_depth , node = stack.pop()

            max_depth = max(cur_depth, max_depth)

            if node.left:
                stack.append([cur_depth + 1, node.left])
            
            if node.right:
                stack.append([cur_depth + 1, node.right])

        return max_depth