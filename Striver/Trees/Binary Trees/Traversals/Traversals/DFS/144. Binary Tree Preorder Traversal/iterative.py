# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        op = []
        stack = [root]

        while stack:
            node = stack.pop()
            op.append(node.val)

            # Append in opposite direction
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return op