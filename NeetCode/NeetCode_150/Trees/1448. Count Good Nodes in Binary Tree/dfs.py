# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        
        max_val = root.val

        self.count += 1

        self.dfs(root.left, max_val)
        self.dfs(root.right, max_val)

        return self.count
    
    def dfs(self, root, max_val):
        if not root:
            return
        
        cur_val = root.val

        # Check if we need to upate the max value
        new_max_val = max_val
        if cur_val >= max_val:
            new_max_val = cur_val
            self.count += 1
        
        self.dfs(root.left, new_max_val)
        self.dfs(root.right, new_max_val)

        return self.count
        

        