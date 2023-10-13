# Inorder: Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        op = []
        self.inorder(root, op)

        # print(op)

        return op[k-1]
    
    def inorder(self, root, op):
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            op.append(node.val)
            root = node.right
        
        return op
            
        