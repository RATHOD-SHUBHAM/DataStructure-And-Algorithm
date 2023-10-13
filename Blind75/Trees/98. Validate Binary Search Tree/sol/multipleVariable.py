# Tc and Sc: O(n)

# This solution failt to analyse depth nodes
# eg: [5,4,6,null,null,3,7]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root)
    
    def isBST(self, root):
        if not root.left and not root.right:
            return True
        
        leftSubTree = True
        rightSubTree = True
        
        if root.left:
            leftSubTree = self.isBST(root.left)
        
        if root.right:
            rightSubTree = self.isBST(root.right)

        Valid_subTree = leftSubTree and rightSubTree
        
        leftNode = True
        rightNode = True
        
        if root.left:
            if root.left.val >= root.val:
                leftNode = False
        
        if root.right:
            if root.val >= root.right.val:
                rightNode = False
        
        return Valid_subTree and leftNode and rightNode
