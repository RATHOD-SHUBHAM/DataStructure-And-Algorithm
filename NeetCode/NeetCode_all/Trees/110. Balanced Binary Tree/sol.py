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

        leftTree = self.bt_height(root.left)
        # print(leftTree)
        rightTree = self.bt_height(root.right)
        # print(rightTree)

        if leftTree == -1 or rightTree == -1 or abs(leftTree - rightTree) > 1:
            return False
        else:
            return True

    def bt_height(self, root):
        if not root:
            return 0
        
        leftTree_height = self.bt_height(root.left)
        # print(leftTree_height)
        rightTree_height = self.bt_height(root.right)
        # print(rightTree_height)

        if leftTree_height == -1 or rightTree_height == -1 or abs(leftTree_height - rightTree_height) > 1:
            return -1
        
        return 1 + max(leftTree_height , rightTree_height)
