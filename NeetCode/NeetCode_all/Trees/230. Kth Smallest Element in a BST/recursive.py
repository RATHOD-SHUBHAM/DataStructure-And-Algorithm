# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_array = []

        self.inorder(root, sorted_array)

        # print(sorted_array)

        return sorted_array[k-1]
    
    def inorder(self, root, sorted_array):
        if not root:
            return

        leftTee = self.inorder(root.left, sorted_array)
        sorted_array.append(root.val)
        rightTree = self.inorder(root.right, sorted_array)

        return