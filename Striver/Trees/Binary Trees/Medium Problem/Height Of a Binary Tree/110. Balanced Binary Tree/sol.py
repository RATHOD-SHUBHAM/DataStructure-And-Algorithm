# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_child_depth = self.height(root.left)
        right_child_depth = self.height(root.right)

        # Check if left subtree and right subtree are balanced
        if left_child_depth == -1 or right_child_depth == -1 or abs(left_child_depth - right_child_depth) > 1:
            return False
        
        return True
    
    def height(self, root):
        if not root:
            return 0

        left_child_depth = self.height(root.left)
        right_child_depth = self.height(root.right)

        # Check if left subtree and right subtree are balanced
        if left_child_depth == -1 or right_child_depth == -1 or abs(left_child_depth - right_child_depth) > 1:
            return -1
        
        # Height of a Binary Tree
        return 1 + max(left_child_depth, right_child_depth)
