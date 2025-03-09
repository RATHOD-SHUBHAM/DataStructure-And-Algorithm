class Solution:
    def __init__(self):
        self.flor = -1
        
    def floor(self, root, x):
        if not root:
            return self.flor
        
        if root.data == x:
            self.flor = root.data
            return self.flor
        elif root.data > x:
            return self.floor(root.left, x)
        else:
            self.flor = root.data
            return self.floor(root.right, x)