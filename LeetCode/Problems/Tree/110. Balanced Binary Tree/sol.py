# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, isBalanced = self.heightBalanced(root)
        return isBalanced
    
    def heightBalanced(self, root):
        if not root:
            return (0 , True)
        
        leftChild_height , isBalaned_leftChild= self.heightBalanced(root.left)
        rightChild_height, isBalanced_rightChild = self.heightBalanced(root.right)

        # claculate height of current tree
        height_of_tree = 1 + max(leftChild_height , rightChild_height)
        
        # check if the subtree of the current tree is balaned
        if not isBalaned_leftChild or not isBalanced_rightChild:
            return (height_of_tree , False)
        
        # check if the current tree is balanced
        if abs(rightChild_height - leftChild_height) > 1:
            return (height_of_tree, False)
        
        return (height_of_tree, True)