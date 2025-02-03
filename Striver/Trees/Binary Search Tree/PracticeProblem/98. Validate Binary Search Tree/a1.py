# ------------------------ Recursive ------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minRange = -math.inf
        maxRange = math.inf
        return self.dfs(root, minRange, maxRange)
    
    def dfs(self, root, minRange, maxRange):
        if not root:
            return True
        
        # Set the range for subtrees
        leftSubTree = self.dfs(root.left, minRange, root.val)
        rightSubTree = self.dfs(root.right, root.val, maxRange)

        # Check the range for current tree
        curTree = True
        if minRange >= root.val or maxRange <= root.val:
            curTree = False

        return leftSubTree and rightSubTree and curTree


# ------------------------ Iterative ------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minRange = -math.inf
        maxRange = math.inf
        
        queue = [[root, minRange, maxRange]]

        while queue:
            node, minRange, maxRange = queue.pop(0)

            # Check the range for current tree
            if minRange >= node.val or maxRange <= node.val:
                return False
            
            # Set the range for subtrees
            if node.left:
                queue.append([node.left, minRange, node.val])
            
            if node.right:
                queue.append([node.right, node.val, maxRange])
        
        return True