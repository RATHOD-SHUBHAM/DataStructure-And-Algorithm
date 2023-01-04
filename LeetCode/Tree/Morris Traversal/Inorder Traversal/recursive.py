# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        op = []
        self.inorder(root, op)
        return op
    
    def inorder(self, root, op):
        if not root:
            return op
        
        self.inorder(root.left , op)
        
        op.append(root.val)
        
        self.inorder(root.right, op)
        
        return