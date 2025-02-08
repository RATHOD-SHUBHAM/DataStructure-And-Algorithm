"""
Using the same find 2 swapped algorithm
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.x = None
        self.y = None
        self.pred = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.inorderTraversal(root)

        # Swap the values
        self.x.val , self.y.val = self.y.val, self.x.val

        return root
    
    def inorderTraversal(self, root):
        if not root:
            return
        
        self.inorderTraversal(root.left)

        # We are at the root
        if self.pred and root.val < self.pred.val:
            self.y = root

            if self.x == None:
                self.x = self.pred
            else:
                return

        self.pred = root

        self.inorderTraversal(root.right)