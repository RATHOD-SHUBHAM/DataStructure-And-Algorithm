# --------------------  Max Depth of Binary Tree  --------------------

# Same as Height of tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        left_tree_height = self.maxDepth(root.left)
        right_tree_height = self.maxDepth(root.right)

        return 1 + max(left_tree_height , right_tree_height)
    
# ------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 0     
        cur_depth = 1

        stack = []
        stack.append([cur_depth, root])

        while stack:
            cur_depth , node = stack.pop()

            max_depth = max(cur_depth, max_depth)

            if node.left:
                stack.append([cur_depth + 1, node.left])
            
            if node.right:
                stack.append([cur_depth + 1, node.right])

        return max_depth
    

# --------------------  Min Depth of Binary Tree  --------------------


# Reursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # if no left child - move right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # if no right child - move left
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both the child are present
        left_tree_height = self.minDepth(root.left)
        right_tree_height = self.minDepth(root.right)
        
        return 1 + min(left_tree_height , right_tree_height)
    
# -----------------------------------------------------------------------

# Iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [[root, 1]]
        
        while queue:
            q_size = len(queue)

            for _ in range(q_size):
                node, depth = queue.pop(0)

                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append([node.left, depth + 1])

                if node.right:
                    queue.append([node.right, depth + 1])
                    
        return -1 