# Same as Height of tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.heightOfTree(root)
    
    def heightOfTree(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftTree = self.heightOfTree(root.left)
        rightTree = self.heightOfTree(root.right)

        height_of_tree = 1 + max(leftTree, rightTree)

        return height_of_tree