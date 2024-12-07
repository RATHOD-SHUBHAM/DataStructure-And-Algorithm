# --------------------  Max Depth of Binary Tree  --------------------

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