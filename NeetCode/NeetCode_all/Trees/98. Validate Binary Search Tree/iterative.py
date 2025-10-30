# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = -math.inf
        high = math.inf

        queue = [(root, low, high)]

        while queue:
            node, low, high = queue.pop(0)

            if node.val <= low or node.val >= high:
                return False
            else:
                # low < node and node < high
                if node.left:
                    queue.append((node.left, low, node.val))
                if node.right:
                    queue.append((node.right, node.val, high))
        
        return True