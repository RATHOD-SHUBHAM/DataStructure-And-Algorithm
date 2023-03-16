# time and space = O(nlogn) || O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return -1

        # get height of root node
        left = self.height(root.left)
        right = self.height(root.right)
        
        # check if subtrees are balanced
        if abs(left - right) < 2 :
            leftSubtree = self.isBalanced(root.left)
            rightSubtree = self.isBalanced(root.right)
            
            if leftSubtree and rightSubtree:
                return True
            
        return False
    
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left , right)