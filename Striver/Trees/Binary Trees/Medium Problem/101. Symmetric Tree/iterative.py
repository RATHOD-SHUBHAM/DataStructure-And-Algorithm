# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = [[root.left, root.right]]

        while queue:
            node_1, node_2 = queue.pop(0)

            if not node_1 and not node_2:
                # Continue because there can other nodes after this
                continue

            if not node_1 or not node_2:
                return False
            
            if node_1.val != node_2.val:
                return False
            
            # Append in symmetrical manner
            queue.append([node_1.left, node_2.right])
            queue.append([node_2.left, node_1.right])
        
        return True


# --------------- Same Solution different way to write ---------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [[root.left, root.right]]

        while stack:
            p , q = stack.pop(0)

            if not p and not q:
                continue

            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            stack.append([p.left, q.right])
            stack.append([p.right, q.left])
        
        return True