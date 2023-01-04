# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        op = []
        stack = []
        
        node = root
        
        while node or len(stack) > 0:
            # Add node to stack
            while node:
                stack.append(node)
                node = node.left
            
            # At this point we reached the leaf node
            node = stack.pop()
            op.append(node.val)
            node = node.right
        
        return op