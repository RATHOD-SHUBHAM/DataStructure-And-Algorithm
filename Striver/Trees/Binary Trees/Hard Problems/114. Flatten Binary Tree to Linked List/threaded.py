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
        
        curNode = root

        while curNode:
            if not curNode.left:
                curNode = curNode.right
            else:
                prevNode = curNode.left
                

                # Move to leftchild's rightmost node
                while prevNode.right:  
                    prevNode = prevNode.right
                
                # Connect the right node to leftchild's rightmost node
                prevNode.right = curNode.right

                # Move the leftchild to right
                curNode.right = curNode.left

                curNode.left = None
