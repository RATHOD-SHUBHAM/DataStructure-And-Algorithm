'''

199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.



'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        stac_k = [root]
        level = []  # to hold the child
        result = []  # final answer

        while stac_k != [] and root is not None:
            for node in stac_k:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            result.append(node.val)
            stac_k = level
            level = []
        return result