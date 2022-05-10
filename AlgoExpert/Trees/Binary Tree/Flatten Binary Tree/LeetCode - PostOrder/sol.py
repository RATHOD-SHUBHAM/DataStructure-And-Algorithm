# Time =  O(n)
# Space = O(1)

'''
            5                       5                   5
           / \                       \                   \
          2   1                       2                   2 
           \  / \                      \                   \
            6 10 11                     6                   6
           /                           / \                   \
          44                          44  1                  44
           \                           \  / \                  \
            23                         23 10 11                23
                                                                \
                                                                 1
                                                                  \   
                                                                  10
                                                                   \
                                                                   11

'''
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
        
        while root:
            # check if the root has left child
            if root.left:
                # get the right most child of left tree
                rightMost = root.left

                while rightMost.right:
                    rightMost = rightMost.right

                # connect the rightmost to right child
                rightMost.right = root.right

                # make the left cild the right child
                root.right = root.left
                root.left = None

            root = root.right
        
        