# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        depth_of_left_subTree = self.depth(root.left)
        depth_of_right_subTree = self.depth(root.right)


        # Check if left subtree and right subtree are balanced
        if depth_of_left_subTree == -1 or depth_of_right_subTree == -1 or abs(depth_of_left_subTree - depth_of_right_subTree) > 1:
            return False
        else:
            return True
    

    def depth(self, root):
        if not root:
            return 0
        
        left_subTree_height = self.depth(root.left)
        right_subTree_height = self.depth(root.right)

        if left_subTree_height == -1 or right_subTree_height == -1 or abs(left_subTree_height - right_subTree_height) > 1:
            return -1
        
        # height of subtree
        return 1 + max(left_subTree_height , right_subTree_height)