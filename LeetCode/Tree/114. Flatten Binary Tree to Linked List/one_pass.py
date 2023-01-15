# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        node = root
        
        while node:
            # get the right most child of the left subtree
            if node.left:
                rightMostChild = node.left
                
                while rightMostChild.right:
                    rightMostChild = rightMostChild.right
                    
                # change the pointer
                rightMostChild.right = node.right
                node.right = node.left
                node.left = None
            
            # move to the child node
            node = node.right
            
        return root