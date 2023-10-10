# Tc: O(n) and Sc: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        leftNode = self.invertTree(root.left)
        rightNode = self.invertTree(root.right)

        # Swap Nodes
        root.left = rightNode
        root.right = leftNode

        return root

# ----------------------------------------------------------------------

# Tc: O(n) and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = collections.deque([root])
        # queue = [root]

        while queue:
            node = queue.popleft()
            # node = queue.pop(0)

            # Swapping
            leftNode = node.left
            rightNode = node.right
            
            node.right = leftNode
            node.left = rightNode

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
        return root
