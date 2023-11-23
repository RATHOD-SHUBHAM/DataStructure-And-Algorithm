# Tc: O(n) and Sc: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        queue = [root]

        while queue:
            node = queue.pop(0)

            # swap nodes
            node.left , node.right = node.right , node.left

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return root