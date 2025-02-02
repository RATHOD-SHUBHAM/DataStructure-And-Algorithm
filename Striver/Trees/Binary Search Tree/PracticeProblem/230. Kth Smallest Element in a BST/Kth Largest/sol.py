# Reverse Inorder

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while stack or root:
            # Move right
            while root:
                stack.append(root)
                root = root.right
            
            node = stack.pop()
            self.count += 1

            root = node.left

            if self.count == k:
                return node.val
        