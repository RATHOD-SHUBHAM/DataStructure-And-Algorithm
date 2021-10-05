# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        s1 = [root]  # odd value
        s2 = []  # even value
        level = []  # pair wise value
        result = []  # final result

        while s1 or s2:
            while s1:
                root = s1.pop(0)
                level.append(root.val)

                if root.left:
                    s2.append(root.left)
                if root.right:
                    s2.append(root.right)

            result.append(level)
            level = []

            while s2:
                root = s2.pop(0)
                level.append(root.val)

                if root.left:
                    s1.append(root.left)
                if root.right:
                    s1.append(root.right)

            if level != []:
                result.append(level)
                level = []

        return result