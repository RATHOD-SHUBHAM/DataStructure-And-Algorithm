# Tc adn Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        if not root:
            return False
        
        stack = [(root, 0)]
        
        while len(stack) > 0:
            node , curSum = stack.pop()
            
            curSum += node.val
            
            if not node.left and not node.right:
                if curSum == targetSum:
                    return True
                
            if node.left:
                stack.append((node.left, curSum))
            
            if node.right:
                stack.append((node.right, curSum))
        
        return False