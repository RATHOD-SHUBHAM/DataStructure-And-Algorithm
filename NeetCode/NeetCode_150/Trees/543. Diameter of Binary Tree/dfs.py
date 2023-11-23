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
        self.treeDiameter(root)
        return self.diameter
    
    def treeDiameter(self, root):

        if not root:
            return 0
        
        left_subtree_diameter = self.treeDiameter(root.left)
        right_subtree_diameter = self.treeDiameter(root.right)

        # Diameter of subtree
        self.diameter = max( self.diameter , (left_subtree_diameter + right_subtree_diameter) ) 

        # Height of SubTree
        return 1 + max(left_subtree_diameter , right_subtree_diameter)
