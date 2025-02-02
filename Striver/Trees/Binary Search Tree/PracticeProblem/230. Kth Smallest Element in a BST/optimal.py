# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.findSmallest(root, k)
    
    def findSmallest(self, root, k):
        stack = []

        while root or stack:
            # Move left
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            self.count += 1

            # Move right
            root = node.right

            if self.count == k:
                return node.val