# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        op = []
        self.preOrder(root, op)
        return op
    
    def preOrder(self, root, op):
        if not root:
            return op
        
        op.append(root.val)
        self.preOrder(root.left, op)
        self.preOrder(root.right , op)
        
        return op