## Better solution than top down approach
# Time and space = O(n) || O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]
    
    def helper(self, root):
        if not root:
            # return is balaned and return height
            return [True, 0]
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        # if left side subtree is balanced and right side subtree is balanced and its height diff is < 2 then the tree is balanced
        balanced = (left[0] and right[0] 
                   and
                   abs(left[1] - right[1]) < 2 )
        
        height = 1 + max(left[1], right[1])
        
        return [balanced, height]