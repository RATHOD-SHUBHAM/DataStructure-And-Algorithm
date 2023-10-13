# Tc and Sc :O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        low = -math.inf
        high = math.inf

        stack = [(root, low, high)]

        while stack:
            node, low, high = stack.pop(0)
            
            if node.val <= low or node.val >= high:
                return False

            if node.left:
                stack.append((node.left, low , node.val))
            
            if node.right:
                stack.append((node.right, node.val, high))
        
        return True

            