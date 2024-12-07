# Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # if no left child - move right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # if no right child - move left
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both the child are present
        left_tree_height = self.minDepth(root.left)
        right_tree_height = self.minDepth(root.right)
        
        return 1 + min(left_tree_height , right_tree_height)