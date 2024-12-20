# --------------------------------------- Recursive  ---------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False
        
        return self.dfs(root.left, root.right)
    
    def dfs(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        
        if not root_1 or not root_2:
            return False
        
        return root_1.val == root_2.val and self.dfs(root_1.left, root_2.right) and self.dfs(root_2.left, root_1.right)


# --------------------------------------- Iterative ---------------------------------------

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

