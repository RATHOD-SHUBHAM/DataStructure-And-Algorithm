# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Tc: O(m + n) | Sc: O(h1 + h2)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # get all the leaf node of tree 1
        leaf_1 = []
        self.getLeaf(root1, leaf_1)
        
        # get all the leaf node of tree 2
        leaf_2 = []
        self.getLeaf(root2, leaf_2)
        
        return leaf_1 == leaf_2
    
    def getLeaf(self, root, leafNode):
        if not root.left and not root.right:
            leafNode.append(root.val)
            return
        
        if root.left:
            self.getLeaf(root.left, leafNode)
            
        if root.right:
            self.getLeaf(root.right, leafNode)
            
        return leafNode