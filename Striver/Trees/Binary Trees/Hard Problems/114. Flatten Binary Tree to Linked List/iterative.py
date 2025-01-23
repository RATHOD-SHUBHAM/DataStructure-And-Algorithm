# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]

        while stack:
            node = stack.pop()

            # Move frrom right to left
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            
            # Creat new tree
            node.left = None
            if stack:
                node.right = stack[-1]
        
        return root