# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.predecessor = None
        self.found_p = False
    
    def inorderPredecessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.inorderTraversal(root, p)
        return None if self.predecessor == False else self.predecessor
    
    def inorderTraversal(self, root, p):
        if not root:
            return
        
        rightTree = self.inorderTraversal(root.right, p)
        

        if self.found_p == True:
            if self.predecessor == None:
                self.predecessor = root
        
        if root.val == p.val:
            self.found_p = True
        
        leftTree = self.inorderTraversal(root.left, p)