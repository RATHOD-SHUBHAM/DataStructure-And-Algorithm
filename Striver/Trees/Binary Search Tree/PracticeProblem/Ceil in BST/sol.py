class Solution:
    def __init__(self):
        self.ceil = -1
        
    def findCeil(self,root, x):
        if not root:
            return self.ceil
        
        if root.key == x:
            self.ceil = root.key
            return self.ceil
        
        if x > root.key:
            return self.findCeil(root.right, x)
        else:
            self.ceil = root.key
            return self.findCeil(root.left, x)