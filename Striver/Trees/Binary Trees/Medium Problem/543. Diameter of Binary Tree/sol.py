# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.height(root)

        return self.diameter
    
    def height(self, root):
        if not root:
            return 0
        
        left_subtree_depth = self.height(root.left)
        right_subtree_depth = self.height(root.right)

        # Diameter of BT
        cur_diameter = left_subtree_depth + right_subtree_depth
        self.diameter = max(self.diameter, cur_diameter)

        # Height of BT
        return 1 + max(left_subtree_depth, right_subtree_depth)