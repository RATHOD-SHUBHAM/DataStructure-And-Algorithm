# Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = [0]
        self.heightBT(root, max_path)
        return max_path[0]
    
    def heightBT(self, root, max_path): 
        if not root:
            return 0
        
        leftTree_height = self.heightBT(root.left, max_path)
        rightTree_height = self.heightBT(root.right, max_path)
        
        max_path[0] = max(max_path[0] , leftTree_height + rightTree_height)
        
        return 1 + max(leftTree_height , rightTree_height)