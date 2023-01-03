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
        
        curSum = 0
        return self.dfs(root, targetSum, curSum)
    
    
    def dfs(self, root, targetSum, curSum):
        newSum = curSum + root.val
        
        if not root.left and not root.right:
            if newSum == targetSum:
                return True
            else:
                return False
        
        leftTree = False
        if root.left:
            leftTree = self.dfs(root.left, targetSum, newSum)
        
        rightTree = False
        if root.right:
            rightTree = self.dfs(root.right, targetSum, newSum)
            
        return leftTree or rightTree