# Tc: O(n) | Sc: O(h)

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

        leftTreeDepth = self.maxDepth(root.left)
        rightTreeDepth = self.maxDepth(root.right)

        return 1 + max(leftTreeDepth, rightTreeDepth)
    

# --------------------------------------------------------------------

# Tc Sc: O(n)

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

        depth = 1
        stack = [[root, depth]]

        max_depth = 0

        while stack:
            node, depth = stack.pop()

            max_depth = max(max_depth, depth)

            if node.left:
                stack.append([node.left, depth + 1])
            
            if node.right:
                stack.append([node.right, depth + 1])
        
        return max_depth