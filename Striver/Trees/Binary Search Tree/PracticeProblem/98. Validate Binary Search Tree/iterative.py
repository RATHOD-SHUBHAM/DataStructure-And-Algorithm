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