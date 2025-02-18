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
    

# --------------------------- Using Max Depth Logic ---------------------------

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
        return self.heightOfTree(root)
    
    def heightOfTree(self, root:Optional[TreeNode]) -> int:
        if not root:
            return math.inf
        
        leftTree = self.heightOfTree(root.left)
        rightTree = self.heightOfTree(root.right)

        childTree = min(leftTree, rightTree)
        child_tree_height = childTree if childTree != math.inf else 0

        height_of_tree = 1 + child_tree_height

        return height_of_tree