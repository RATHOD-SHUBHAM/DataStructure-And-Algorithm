# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, False)
    
    def helper(self, root, parentRobbed):
        if not root:
            return 0
        
        if parentRobbed:
            return self.helper(root.left , False) + self.helper(root.right , False)
        
        else:
            # rob = root + grabdchild
            rob = root.val + self.helper(root.left , True) + self.helper(root.right , True)

            # dont rob
            dont_rob = self.helper(root.left , False) + self.helper(root.right , False)
            
            return max(rob, dont_rob)