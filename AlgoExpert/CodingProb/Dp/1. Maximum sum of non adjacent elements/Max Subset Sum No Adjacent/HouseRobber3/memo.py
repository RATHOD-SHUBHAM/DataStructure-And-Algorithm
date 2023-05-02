# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo_parent_robbed = {}
        memo_parent_not_robbed = {}
        return self.helper(memo_parent_robbed, memo_parent_not_robbed, root, False)
    
    def helper(self, memo_parent_robbed, memo_parent_not_robbed, root, parentRobbed):
        if not root:
            return 0
        
        if parentRobbed:
            if root in memo_parent_robbed:
                return memo_parent_robbed[root]
            
            result = self.helper(memo_parent_robbed, memo_parent_not_robbed, root.left , False) + self.helper(memo_parent_robbed, memo_parent_not_robbed, root.right , False)
            
            memo_parent_robbed[root] = result
            return result
        
        else:
            # rob = root + grabdchild
            rob = root.val + self.helper(memo_parent_robbed, memo_parent_not_robbed, root.left , True) + self.helper(memo_parent_robbed, memo_parent_not_robbed, root.right , True)

            # dont rob
            dont_rob = self.helper(memo_parent_robbed, memo_parent_not_robbed, root.left , False) + self.helper(memo_parent_robbed, memo_parent_not_robbed, root.right , False)
            
            result = max(rob, dont_rob)
            
            memo_parent_not_robbed[root] = result
            
            return result