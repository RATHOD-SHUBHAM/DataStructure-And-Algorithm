# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        leftChild = root.left
        rightChild = root.right

        return self.helper(leftChild, rightChild)
    
    def helper(self, leftChild, rightChild):
        if leftChild and rightChild: # is not None
            return leftChild.val == rightChild.val and self.helper(leftChild.left,rightChild.right) and self.helper(leftChild.right,rightChild.left)
        
        if (not leftChild and rightChild) or (leftChild and not rightChild):
            return False
        else:
            return True
            