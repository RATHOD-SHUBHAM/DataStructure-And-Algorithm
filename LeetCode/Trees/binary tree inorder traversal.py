'''
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

'''
# ==============================================================================
# todo : Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        while root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)




# ==============================================================================
# todo : Iteration

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []

        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result