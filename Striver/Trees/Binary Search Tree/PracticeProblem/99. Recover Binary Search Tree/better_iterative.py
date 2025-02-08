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
        curNode = root
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()

            if self.pred and node.val < self.pred.val:
                self.y = node

                if self.x == None:
                    self.x = self.pred
                else:
                    break
            
            self.pred = node

            root = node.right
        
        return