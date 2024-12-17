# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        
        if not root.left or not root.right:
            return False
        
        queue = [root.left, root.right]

        while queue:
            node_one = queue.pop(0)
            node_two = queue.pop(0)

            if not node_one and not node_two:
                continue

            if not node_one or not node_two:
                return False
        
            
            if node_one.val != node_two.val:
                return False

            
            # node_one -> Left child, node_two -> Right Child
            queue.append(node_one.left)
            queue.append(node_two.right)

            # node_one -> Right child, node_two -> Left Child
            queue.append(node_one.right)
            queue.append(node_two.left)

        
        return True
