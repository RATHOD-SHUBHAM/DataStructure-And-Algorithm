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
        self.dfs(root)
        
        return root
    
    def dfs(self, node):
        if not node:
            return
        
        if not node.left and not node.right:
            return node
        
        leftChild = self.dfs(node.left) # get the right most node
        rightChild = self.dfs(node.right)
        
        if leftChild:
            # right most node of leftchild will point to rightchild
            leftChild.right = node.right
            # change the nodes pointer
            node.right = node.left
            node.left = None
            
        return rightChild if rightChild else leftChild
        