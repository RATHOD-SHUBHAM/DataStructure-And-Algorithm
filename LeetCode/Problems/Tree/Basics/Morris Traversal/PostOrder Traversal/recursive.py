# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        op = []
        self.postorder(root, op)
        return op
    
    def postorder(self, root, op):
        # base case
        if not root:
            return op
        
        self.postorder(root.left, op)
        self.postorder(root.right, op)
        op.append(root.val)
        
        return