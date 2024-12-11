# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = -math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.dfs(root)

        return self.maxSum
    
    def dfs(self, root):
        if not root:
            return 0
        
        left_subtree_sum = self.dfs(root.left)
        left_subtree_sum = max(0, left_subtree_sum) # Handle negative value

        right_subtree_sum = self.dfs(root.right)
        right_subtree_sum = max(0, right_subtree_sum) # Handle negative value

        # Subtrees sum
        cur_sum = root.val + left_subtree_sum + right_subtree_sum
        self.maxSum = max(self.maxSum, cur_sum)

        # Max Path Sum for the current tree
        return root.val + max(left_subtree_sum , right_subtree_sum)